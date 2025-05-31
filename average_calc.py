def average_calc(ls):
    downloads = []
    uploads = []

    for item in ls:
        for key, value in item.items():
            try:
                float_value = float(value)
                if key.startswith("download"):
                    downloads.append(float_value)
                elif key.startswith("upload"):
                    uploads.append(float_value)

            except ValueError:
                continue


    average_download_speed = (sum(downloads)/len(downloads))
    average_upload_speed = (sum(uploads)/len(uploads))

    return {
        "average_download": average_download_speed,
        "average_upload": average_upload_speed
    }