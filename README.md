# Vera
Rolling update framework for Monika After Story. TBD

## Architecture

Vera is designed to be executed as a child process for MAS, and is responsible for rolling updates.

Rolling updates is by default the update strategy of vera since we only update when the client is closed, or has the consent to have a blocking update.


**Background updates**

Vera performs a background update and searches for a new version every hour. This is relatively light on bandwidth, however, when update is found, the updater finds a ZIP file suffixed in the filename `-vera{{patch_version}}`, where ``{{patch_version}}`` is a ordinal designation.

**Security**

By default, Vera requires you to have a key inside the ZIP file for security purposes. This is to authenticate and verify the update is a valid trust source. If you have a CI, kindly add your key so Vera knows what ZIP file to accept. ZIP files must be delta-compressed during download as well with hash integrity checks.
