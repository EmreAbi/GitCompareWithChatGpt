# Repository File Comparison Tool

## Description

This Python script allows users to compare files and directories between different branches of a Git repository. It provides the flexibility to use different comparison tools (Beyond Compare and OpenAI's GPT-3) and offers the possibility to compare either entire directories or individual files. This tool can be particularly useful for developers and reviewers who need to understand changes made across different branches of a repository, with a focus on code changes.

## Features

- Selection of a specific subdirectory of the Git repository for comparison.
- The ability to ignore certain files or directories during comparison.
- Comparison of files and directories between two branches of the repository.
- Using different comparison tools: Beyond Compare for a visual side-by-side comparison and OpenAI's GPT-3 model for a natural language description of changes.
- Normalization of the files' content to create a readable prompt for the AI model.

## Prerequisites

Before you can run the script, you need to install the following Python libraries:

- `filecmp` (standard library): for file and directory comparisons.
- `os` (standard library): for OS interactions, such as environment variable access and path manipulations.
- `shutil` (standard library): for high-level file operations.
- `subprocess` (standard library): to allow running of Beyond Compare from the script.
- `openai`: to interact with the OpenAI API and use GPT-3 for text generation.
- `inquirer`: to create a user-friendly command-line interface.
- `gitpython`: to interact with the Git repository.

You can install the required libraries with pip:

```bash
pip install openai inquirer gitpython
```

You also need to have Beyond Compare installed on your system if you plan to use it as a comparison tool.

## Usage

1. Ensure that your OpenAI API key is set in your environment variables.
2. Update the repo_path variable in the script to point to the root directory of your Git repository.
3. Run the script. It will prompt you to choose a subdirectory, and then two branches for comparison.
4. You'll then be prompted to select the scope of your comparison - either individual files or whole folders.
5. If you select 'Files', you'll be asked to choose a comparison tool. You can select either Beyond Compare for a visual side-by-side comparison or ChatGPT for a text description of the changes.
6. If you choose Beyond Compare, the tool will open and display differences for the selected file. If you choose ChatGPT, it will generate a text description of the changes and save it as a .txt file.
7. If there are no differences, the script will notify you and exit.

## Limitations
Please note that this script has been developed and tested on a Windows environment. While it should work on other platforms, some functionality, such as the subprocess call to Beyond Compare, may require modification to function correctly on non-Windows operating systems.

## Contributing
Contributions are welcome! If you encounter any issues or have features you'd like to see implemented, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
