import sys
print(sys.executable)


from huggingface_hub import snapshot_download

def download():
    snapshot_download(repo_id= "llSourcell/doctorGPT_mini")

if __name__ == '__main__':
    download()