package main

import (
    "fmt"
    "os/exec"
	"bytes"
)

func executeCommand(command string) (string, string, error) {
    // Create a new command execution
    cmd := exec.Command("sh", "-c", command)
    
    // Capture stdout and stderr separately
    var stdout bytes.Buffer
    var stderr bytes.Buffer
    
    // Set up pipes for stdout and stderr
    cmd.Stdout = &stdout
    cmd.Stderr = &stderr
    
    // Execute the command
    err := cmd.Run()
    
    if err != nil {
        return "", "", fmt.Errorf("error executing command: %v", err)
    }
    
    return stdout.String(), stderr.String(), nil
}

func main() {
    // Example usage
    command := "ls -l"
    stdout, stderr, err := executeCommand(command)
    
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    
    fmt.Printf("Command executed successfully\n")
    fmt.Println("stdout:")
    fmt.Println(stdout)
    fmt.Println("stderr:")
    fmt.Println(stderr)
}
