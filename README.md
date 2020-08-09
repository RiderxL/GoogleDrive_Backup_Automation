FUNCTIONS
    -- Upload
    -- Download
    -- Create
    -- List

gauth.SaveCredentialsFile(credential_file)

        drive = GoogleDrive(gauth)
        folder_id = os.getenv('GOOGLE_DRIVE_FOLDER_ID')
        filename_w_ext = os.path.basename(file_path)
        filename, file_extension = os.path.splitext(filename_w_ext)

        # Upload file to folder
        f = drive.CreateFile(
            {"parents": [{"kind": "drive#fileLink", "id": folder_id}]})
        f['title'] = filename_w_ext

        # Make sure to add the path to the file to upload below.
        f.SetContentFile(file_path)
        f.Upload()

        logger.info(f['id'])
        return f['id']
    except Exception:
        logger.exception('Failed to upload %s', file_path)
    # end try
    return None