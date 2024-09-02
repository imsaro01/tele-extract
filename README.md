# Telegram Channel File Scrapper

# Overview

This script downloads files from specified Telegram channels using the Telegram API. It supports downloading files with specific extensions and handles both single and multiple channels. The script also includes robust logging and maintains a summary of downloaded files in JSON format.

# Features

- **Download Files**: Automatically downloads files with specified extensions (`.zip`, `.7z`, `.txt`, `.rar`) from Telegram channels.
- **Handle Multiple Channels**: Supports downloading from one or more channels.
- **Rate Limiting**: Implements rate limiting to handle Telegram's API constraints.
- **Logging**: Logs actions and errors to both the console and a log file.
- **Summary**: Maintains a JSON summary of downloaded files and their types.
- **Configuration**: Easily configurable via a `config.ini` file.

# Requirements

- Python 3.7 or higher
- `telethon` library
- Your Telegram API credentials

# Installation

1. **Clone the repository** (if applicable) or download the script.

2. **Install Dependencies**:
   Ensure you have `telethon` installed. You can install it using pip:

   ```bash
   pip install telethon
   ```

3. **Configuration**:
   Create a `config.ini` file in the same directory as the script with the following structure:

   ```ini
   [Telegram]
   API_ID = your_api_id
   API_HASH = your_api_hash
   PHONE_NUMBER = your_phone_number
   CHANNEL_USERNAME = channelname  # Comma-separated list of channel username
   FILE_EXTENSIONS = .zip,.7z,.txt,.rar  # Comma-separated list of file extensions to download
   ```

   Replace `your_api_id`, `your_api_hash`, and `your_phone_number` with your Telegram API credentials and phone number.

4. **Create Required Directories**:
   The script will create the necessary directories (`logs` for logs and `summaries` for the summary file) automatically.

# Usage

Run the script using Python:

```bash
python your_script_name.py
```

Replace `your_script_name.py` with the name of your script file.

# File Structure

- `your_script_name.py`: The main script file.
- `config.ini`: Configuration file with your Telegram API credentials and channel details.
- `logs/`: Directory where log files are stored.
- `summaries/`: Directory where the summary JSON file is stored.

# Log Files

Logs are written to `logs/app.log`. This includes information about the downloading process and any errors encountered.

# Summary File

The summary of downloaded files is stored in `summaries/summary.json`. This file includes counts of files downloaded, categorized by file extension.

# Error Handling

- **Rate Limiting**: The script automatically handles rate limits imposed by Telegram by pausing execution when necessary.
- **Two-Factor Authentication**: If two-factor authentication (2FA) is enabled on your Telegram account, you will be prompted to enter the code.

# Troubleshooting

- Ensure your `config.ini` file is correctly formatted and contains valid Telegram API credentials.
- Make sure the directories specified in the script can be created and written to.
- If you encounter issues, check `logs/app.log` for detailed error messages.

# License

This script is licensed under the Apache License 2.0. See the LICENSE section below for more details.

### Apache License 2.0

```
                               Apache License
                         Version 2.0, January 2004
                      http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.
      "License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.
      "Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.
      "You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.
      "Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation, and configuration files.
      "Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.
      "Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as described in the Source form.
      "Derivative Works" shall mean any work that is based on the Work and for which the Work has been modified, augmented, or otherwise transformed.
      "Contribution" shall mean any work of authorship that is submitted by You to the Licensor for inclusion in the Work.

   2. Grant of Copyright License.
      Subject to the terms and conditions of this License, Licensor hereby grants You a worldwide, royalty-free, non-exclusive, perpetual license to use, reproduce, modify, distribute, and publicly display the Work and Derivative Works.

   3. Grant of Patent License.
      Subject to the terms and conditions of this License, Licensor hereby grants You a worldwide, royalty-free, non-exclusive, perpetual license to make, use, sell, and distribute the Work and Derivative Works without any infringement of the Licensor’s patents.

   4. Redistribution.
      You may reproduce and distribute copies of the Work or Derivative Works in any form, including as part of a larger work, provided that the following conditions are met:
      - You must include a copy of this License with every copy or substantial portion of the Work.
      - You must provide prominent attribution to the Licensor in the Source form of any redistributed Work.

   5. Submission of Contributions.
      If you submit any Contributions to the Licensor, you grant the Licensor a worldwide, royalty-free, non-exclusive, perpetual license to use, reproduce, modify, distribute, and publicly display those Contributions in the Work.

   6. Trademarks.
      This License does not grant you permission to use the trademarks, service marks, or other identifiers of the Licensor except as necessary for complying with the attribution requirements of this License.

   7. Disclaimer of Warranty.
      The Work is provided "as-is" without warranty of any kind. The Licensor makes no warranties regarding the Work, including but not limited to implied warranties of merchantability or fitness for a particular purpose.

   8. Limitation of Liability.
      In no event shall the Licensor be liable for any damages arising out of the use or inability to use the Work, including but not limited to direct, indirect, incidental, or consequential damages.

   9. Accepting the License.
      By using, reproducing, or distributing the Work, you accept the terms and conditions of this License.

   END OF TERMS AND CONDITIONS
```

## Contact

For any questions or issues, please open an issue on the GitHub repository (if applicable) or contact the author at saravanansaro01@outlook.com.

---

Thank you for using the tele-extract! If you find this script useful, please consider giving it a star on GitHub or sharing it with others.
