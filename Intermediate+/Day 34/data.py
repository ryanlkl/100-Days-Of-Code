import requests

trivia_categories = [
    {
      "id": 9,
      "name": "General Knowledge"
    },
    {
      "id": 10,
      "name": "Entertainment: Books"
    },
    {
      "id": 11,
      "name": "Entertainment: Film"
    },
    {
      "id": 12,
      "name": "Entertainment: Music"
    },
    {
      "id": 13,
      "name": "Entertainment: Musicals & Theatres"
    },
    {
      "id": 14,
      "name": "Entertainment: Television"
    },
    {
      "id": 15,
      "name": "Entertainment: Video Games"
    },
    {
      "id": 16,
      "name": "Entertainment: Board Games"
    },
    {
      "id": 17,
      "name": "Science & Nature"
    },
    {
      "id": 18,
      "name": "Science: Computers"
    },
    {
      "id": 19,
      "name": "Science: Mathematics"
    },
    {
      "id": 20,
      "name": "Mythology"
    },
    {
      "id": 21,
      "name": "Sports"
    },
    {
      "id": 22,
      "name": "Geography"
    },
    {
      "id": 23,
      "name": "History"
    },
    {
      "id": 24,
      "name": "Politics"
    },
    {
      "id": 25,
      "name": "Art"
    },
    {
      "id": 26,
      "name": "Celebrities"
    },
    {
      "id": 27,
      "name": "Animals"
    },
    {
      "id": 28,
      "name": "Vehicles"
    },
    {
      "id": 29,
      "name": "Entertainment: Comics"
    },
    {
      "id": 30,
      "name": "Science: Gadgets"
    },
    {
      "id": 31,
      "name": "Entertainment: Japanese Anime & Manga"
    },
    {
      "id": 32,
      "name": "Entertainment: Cartoon & Animations"
    }
  ]

class Data:

    def __init__(self,category,no_questions,difficulty):
        self.category = self.find_category_id(category)
        self.no_questions = int(no_questions)
        self.difficulty = difficulty.lower()
        self.base_url = "https://opentdb.com/api.php"
        self.question_bank = self.send_request()

    def send_request(self):
        url = f"{self.base_url}?amount={self.no_questions}&category={self.category}&difficulty={self.difficulty}&type=boolean"
        response = requests.get(url=url)
        response.raise_for_status()
        data = response.json()
        return data["results"]

    def find_category_id(self,category):
        global trivia_categories
        for c in trivia_categories:
            if c["name"].lower() == category.lower():
                return c["id"]
