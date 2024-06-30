# Tasuke

![Build CI](https://github.com/nthnn/tasuke/actions/workflows/build_ci.yml/badge.svg)

Tasuke is a customizable personal computer assistant that utilizes AI voice command recognition to help automate tasks and provide a more interactive computing experience. This project uses Google Text-to-Speech (gTTS), Pygame for audio playback, and the SpeechRecognition library for capturing and transcribing voice commands.

- **Voice Command Recognition**: Uses Google's speech recognition API to transcribe voice commands.
- **Text-to-Speech**: Provides auditory feedback using gTTS and Pygame.
- **Command Execution**: Executes predefined commands based on recognized phrases.
- **Customizable Commands**: Easily add or modify commands through a configuration file.

## Installation

To get started with Tasuke, follow these comprehensive steps to download, install, and run the software on your system.

1. **Download Tasuke** - Download the Debian package of Tasuke from the official [release page](https://github.com/nthnn/tasuke/releases).

2. **Install the Debian Package** - Once the package is downloaded, install it using the `dpkg` command:

    ```shell
    sudo dpkg -i tasuke_*.deb
    ```

3. **Install APT Dependencies** - Tasuke relies on several system-level dependencies that must be installed before running the script.

    ```shell
    sudo apt install python3-full libespeak-dev portaudio19-dev python3-pyaudio
    ```

4. **Install Python libraries** - Tasuke requires several Python libraries to function properly. Install these dependencies using the following command:

    ```shell
    pip install SpeechRecognition pyaudio gtts pygame setuptools --break-system-packages
    ```

5. **Run Tasuke** - After successfully installing Tasuke and the required dependencies, you can start the application by simply typing tasuke in your terminal:

    ```shell
    tasuke
    ```

    This command initializes Tasuke, and it will begin listening for voice commands based on the configured settings.

## Running from Source

To run Tasuke from source, follow these steps to ensure all dependencies are installed, the necessary configurations are made, and the script is executed correctly.

1. **Install APT Dependencies** - Tasuke relies on several system-level dependencies that must be installed before running the script.

    ```shell
    sudo apt install python3-full libespeak-dev portaudio19-dev python3-pyaudio
    ```

2. **Install Python libraries** - Tasuke requires several Python libraries to function properly. Install these dependencies using the following command:

    ```shell
    pip install SpeechRecognition pyaudio gtts pygame setuptools --break-system-packages
    ```

3. **Configuration File** - Tasuke uses a JSON configuration file to define the voice commands it recognizes and the corresponding actions it performs. Create the configuration file at `/etc/tasuke/conf.d/commands.json` with the following content:

    ```js
    [
      [
        ["what's the date today"],  // Speech transcriptions
        ["Here's the date today"],  // List of possible replies
        "date"                      // Command to be executed
      ]
    ]
    ```

    - **Speech Transcriptions**: A list of phrases that Tasuke will recognize.
    - **List of Possible Replies**: Possible responses Tasuke will randomly give upon recognizing a phrase.
    - **Command to be Executed**: The shell command that Tasuke will execute when a phrase is recognized.

4. **Running the script** - After creating the `commands.json` configuration file, you can now run Tasuke. Use the following command to start the script, redirecting any errors to `/dev/null` to suppress unnecessary error messages:

    ```shell
    python3 tasuke.py 2>/dev/null
    ```

## License

This file is part of the [tasuke](https://github.com/nthnn/tasuke) project.

```
Copyright (c) 2024 Nathanne Isip.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.
 
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
```