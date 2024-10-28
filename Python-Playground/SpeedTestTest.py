import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()

print(f"download speed: {download}")
print(f"upload speed: {upload}")