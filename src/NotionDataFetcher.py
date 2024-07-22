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

    def send_to_notion(
            self,
            apply_number,
            student_id,
            name,
            major,
            status,
            license_info,
            no_license_info,
            first_ingredient,
            detailed_classification,
            purpose,
            second_ingredient,
            third_ingredient,
            receptionist
    ):
        print(major)
        print(status)
        print(no_license_info)
        print(first_ingredient)
        print(purpose)
        print(second_ingredient)
        print(third_ingredient)
        print(receptionist)

        print('send_to_notion')
        print('db id: ', end ="")
        print(self.database_id)
        try:
            self.data = {
                "parent": {"database_id": self.database_id},
                "properties": {
                    "신청 번호": {
                        "title": [  # rich_text 형식으로 변경
                            {
                                "text": {
                                    "content": apply_number
                                }
                            }
                        ]
                    },

                    "상태": {
                        "select": {  # select 형식으로 변경
                            "name": "사용 중"
                        }
                    },

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

                    "학부": {
                        "select": {  # select 형식으로 변경
                            "name": major
                        }
                    },

                    "신분": {
                        "select": {  # select 형식으로 변경
                            "name": status
                        }
                    },

                    "사용분류": {
                        "select": {  # select 형식으로 변경
                            "name": detailed_classification
                        }
                    },

                    "사용 목적 및 특이사항": {
                        "rich_text": [  # rich_text 형식으로 변경
                            {
                                "text": {
                                    "content": purpose
                                }
                            }
                        ]
                    },

                    "공구 및 재료": {
                        "rich_text": [  # rich_text 형식으로 변경
                            {
                                "text": {
                                    "content": first_ingredient
                                }
                            }
                        ]
                    },

                    "공구 및 재료2": {
                        "rich_text": [  # rich_text 형식으로 변경
                            {
                                "text": {
                                    "content": second_ingredient
                                }
                            }
                        ]
                    },

                    "공구 및 재료3": {
                        "rich_text": [  # rich_text 형식으로 변경
                            {
                                "text": {
                                    "content": third_ingredient
                                }
                            }
                        ]
                    },
                }
            }

            if license_info != "":
                self.data["properties"]["장비(라이센스O)"] = {
                    "select": {  # select 형식으로 변경
                        "name": license_info
                    }
                }

            if no_license_info != "":
                self.data["properties"]["장비(라이센스X)"] = {
                    "select": {  # select 형식으로 변경
                        "name": no_license_info
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