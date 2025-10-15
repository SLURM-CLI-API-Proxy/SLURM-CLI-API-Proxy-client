import argparse

def parse_scontrol_command():
    parser = argparse.ArgumentParser(description='Parse scontrol command-line options and commands.')
    
    # Define valid options
    parser.add_argument('-a', '--all', action='store_true', help='Equivalent to "all" command')
    parser.add_argument('-d', '--details', action='store_true', help='Equivalent to "details" command')
    parser.add_argument('--federation', action='store_true', help='Report federated job information')
    parser.add_argument('-F', '--future', action='store_true', help='Report information about nodes in FUTURE state')    
    parser.add_argument('--hide', action='store_true', help='Equivalent to "hide" command')
    parser.add_argument('--json', nargs='?', const='default', help='Produce JSON output')
    parser.add_argument('--local', action='store_true', help='Report information only about local jobs')
    parser.add_argument('-M', '--cluster', action='store_true', help='Equivalent to "cluster" command')
    parser.add_argument('-o', '--oneliner', action='store_true', help='Equivalent to "oneliner" command')
    parser.add_argument('-Q', '--quiet', action='store_true', help='Equivalent to "quiet" command')
    parser.add_argument('--sibling', action='store_true', help='Report information about sibling jobs')
    parser.add_argument('-u', '--uid', type=int, help='Update job as user "uid"')
    parser.add_argument('-v', '--verbose', action='store_true', help='Equivalent to "verbose" command')
    parser.add_argument('-V', '--version', action='store_true', help='Equivalent to "version" command')
    parser.add_argument('--yaml', nargs='?', const='default', help='Produce YAML output')
    
    # Define valid commands
    parser.add_argument('command', nargs='?', choices=[
        'abort', 'all', 'cancel_reboot', 'cluster', 'completing', 'create', 'details', 'delete', 'errnumstr',
        'exit', 'fsdampeningfactor', 'help', 'hold', 'holdu', 'hide', 'listpids', 'notify', 'oneliner',
        'pidinfo', 'ping', 'quiet', 'quit', 'reboot', 'reconfigure', 'release', 'requeue', 'requeuehold',
        'resume', 'setdebug', 'setdebugflags', 'schedloglevel', 'show', 'shutdown', 'suspend', 'top',
        'token', 'takeover', 'uhold', 'update', 'verbose', 'version', 'wait_job', 'write'
    ], help='scontrol command to execute', default=None)
    
    # Special handling for "update" command to accept key-value pairs
    parser.add_argument('subcommand_args', nargs='*', help='Command arguments')
    
    # Parse arguments
    args = parser.parse_args()
    
    # If command is "update", parse key-value pairs into a dictionary
    #if args.command == 'update' and args.updates:
    #    args.updates = dict(pair.split('=') for pair in args.updates if '=' in pair)
    #if args.command == "release"
    
    # Output the parsed arguments
    return vars(args)

if __name__ == "__main__":
    parsed_args = parse_scontrol_command()
    print(parsed_args)