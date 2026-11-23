"""Value converters for sbatch options whose CLI format differs from the API's.

They are available to the ``lambda_expression`` entries in the mapping YAML
files, e.g.::

    api_mapping:
      request_property: job.memory_per_node
      lambda_expression: "lambda p: memory_to_mb_no_val(p)"
"""
import math
import re
from typing import Any, Dict

_MEM_UNITS = {"K": 1 / 1024, "M": 1, "G": 1024, "T": 1024 * 1024}


def no_val(number: int, infinite: bool = False) -> Dict[str, Any]:
    """A Slurm *_NO_VAL struct (e.g. v0.0.43_uint32_no_val_struct)."""
    return {"set": True, "infinite": infinite, "number": 0 if infinite else int(number)}


def memory_to_mb(value: str) -> int:
    """Slurm memory size ('500', '500M', '4G', '1T', '4GB') to megabytes.

    As in sbatch, a number without unit means megabytes.
    """
    m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*([KMGT]?)B?\s*", str(value), re.IGNORECASE)
    if not m:
        raise ValueError(f"invalid memory size: {value!r}")
    number, unit = float(m.group(1)), (m.group(2) or "M").upper()
    return max(1, math.ceil(number * _MEM_UNITS[unit]))


def memory_to_mb_no_val(value: str) -> Dict[str, Any]:
    return no_val(memory_to_mb(value))


def time_to_minutes(value: str) -> int:
    """Slurm time limit to minutes.

    Accepted formats (as sbatch --time): "minutes", "minutes:seconds",
    "hours:minutes:seconds", "days-hours", "days-hours:minutes" and
    "days-hours:minutes:seconds". Seconds are rounded up to whole minutes.
    """
    v = str(value).strip()
    days = 0
    if "-" in v:
        d, v = v.split("-", 1)
        days = int(d)
        parts = [int(p) for p in v.split(":")]
        # days-hours[:minutes[:seconds]]
        parts += [0] * (3 - len(parts))
        hours, minutes, seconds = parts
    else:
        parts = [int(p) for p in v.split(":")]
        if len(parts) == 1:
            hours, minutes, seconds = 0, parts[0], 0
        elif len(parts) == 2:
            hours, minutes, seconds = 0, parts[0], parts[1]
        elif len(parts) == 3:
            hours, minutes, seconds = parts
        else:
            raise ValueError(f"invalid time limit: {value!r}")
    total = days * 24 * 60 + hours * 60 + minutes + (1 if seconds > 0 else 0)
    return total


def time_to_minutes_no_val(value: str) -> Dict[str, Any]:
    if str(value).strip().upper() in ("UNLIMITED", "INFINITE", "-1"):
        return no_val(0, infinite=True)
    return no_val(time_to_minutes(value))


def gres_to_tres(value: str) -> str:
    """sbatch --gres ('gpu:2', 'gpu:a100:1,shard:2') to TRES ('gres/gpu:2,...')."""
    items = [g.strip() for g in str(value).split(",") if g.strip()]
    return ",".join(g if g.startswith("gres/") else f"gres/{g}" for g in items)


# Names usable inside mapping lambda expressions
CONVERTERS = {
    "no_val": no_val,
    "memory_to_mb": memory_to_mb,
    "memory_to_mb_no_val": memory_to_mb_no_val,
    "time_to_minutes": time_to_minutes,
    "time_to_minutes_no_val": time_to_minutes_no_val,
    "gres_to_tres": gres_to_tres,
}
