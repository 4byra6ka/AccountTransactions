from utils.utils import load_operations

url_operations = "https://skyengpublic.notion.site/signed/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd22c7143-d55e-4f1d-aa98-e9b15e5e5efc%2Foperations.json?id=f11058ed-10ad-42ea-a13d-aad1945e5421&table=block&spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&name=operations.json&cache=v2"

load_operations(url_operations)

print(load_operations(url_operations))


