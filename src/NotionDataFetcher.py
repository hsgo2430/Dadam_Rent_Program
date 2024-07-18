import requests
from PyQt5.QtWidgets import QMessageBox
import json


class NotionDataFetcher:
    def __init__(self, token, database_id):
        self.token = token
        self.database_id = database_id
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Notion-Version': '2022-06-28',
            'Content-Type': 'application/json'
        }
        self.data = {}

    def GetData(self):
        return self.data

    def send_to_notion(self, student_id, name, license_info):
        print('send_to_notion')
        print('db id: ', end ="")
        print(self.database_id)
        try:
            self.data = {
                "parent": {"database_id": self.database_id},
                "properties": {
                    "학번": {
                        "number": int(student_id)  # 숫자 형식으로 변경
                    },
                    "이름": {
                        "rich_text": [  # rich_text 형식으로 변경
                            {
                                "text": {
                                    "content": name
                                }
                            }
                        ]
                    },
                    "장비(라이센스O)": {
                        "select": {  # select 형식으로 변경
                            "name": license_info
                        }
                    }
                }
            }
            print(f'self.data : {self.data}')
            response = requests.post(
                'https://api.notion.com/v1/pages',
                headers=self.headers,
                data=json.dumps(self.data)
            )
            print(f'response : {response}')
            print(f'response content: {response.content}')
            return response.status_code == 200
        except Exception as e:
            print(f'Notion 오류가 발생했습니다: {str(e)}')
            return False