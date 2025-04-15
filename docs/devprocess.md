# Continious integration

This repository 


# Version Management

## Overview
This project uses trunk-based development with controlled releases. Versions are managed through a combination of semantic versioning and feature flags.

```mermaid
sequenceDiagram
    participant D as Developer
    participant M as Main Branch
    participant R as Release Branch
    participant P as Production
    
    Note over D,P: Version Management Workflow
    
    D->>M: Direct commit to main
    activate M
    Note over M: Run CI/CD pipeline
    alt Pipeline passes
        M->>P: Deploy to production
    else Pipeline fails
        P-->>M: Fix issues
        M->>P: Retry deployment
    end
    
    
    Note over M,R: Ready for release
    M->>R: Create release branch
    activate R
    Note over R: Update version in setup.py
    Note over R: Stabilize & prepare release
    R->>P: Deploy release
    deactivate R
    
    Note over P,M: Post-release
    P-->>M: Backmerge release changes
    Note over M: Increment version for next dev
    deactivate M
```

## Version Update Process
### When to Update Versions
- Update version in setup.py during release branch creation
- Increment version in main branch after release
- Use semantic versioning (major.minor.patch)

### Release Workflow
1. Create release branch from main
2. Update version in setup.py
3. Stabilize and test
4. Deploy to production
5. Merge back to main
6. Increment version for next development cycle

## Main Branch Management
- Keep main branch always releasable
- Use feature flags for incomplete features
- Document version changes in changelog
- Maintain clear version history