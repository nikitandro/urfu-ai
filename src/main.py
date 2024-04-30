#!/usr/bin/env python3

import ai


if __name__ == '__main__':
    try:
        while True:
            query = input("Запрос> ")
            if query == "exit":
                break
            if not query:
                continue
            query = ai.translate(query)
            print("Query:", query)
            response = ai.classify(query)
            print("Response:", response)
    except (KeyboardInterrupt, EOFError):
        print("Exiting...")
