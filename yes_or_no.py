#!/usr/bin/env python3

def yes_or_no(question):
    while True:
        answer = input(question + ' (y/n): ').lower().strip()
        if answer in ('y', 'yes', 'n', 'no'):
            return answer in ('y', 'yes')
        else:
            print('You must answer yes or no.')

if __name__ == '__main__':
  yes_or_no('yes or no?')
