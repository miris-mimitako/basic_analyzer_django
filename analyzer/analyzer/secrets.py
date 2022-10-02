from django.core.management.utils import get_random_secret_key
import json
import os
from pathlib import Path

class SecretsGen:
  def __init__(self) -> None:
    pass

  def gen_key(self):
    file_path = Path(__file__).resolve().parent
    secrets = get_random_secret_key()
    open_json = open(os.path.join(file_path,".secrets.json"), "w")
    json_writer = {"secretkey":secrets}
    json.dump(json_writer, open_json, indent=2)
    open_json.close()
  
  def __del__(self):
    pass


if __name__=="__main__":
  pass
