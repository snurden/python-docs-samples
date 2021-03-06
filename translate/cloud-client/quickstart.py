#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def run_quickstart():
    # [START translate_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import translate

    # Your Translate API key
    api_key = 'YOUR_API_KEY'

    # Instantiates a client
    translate_client = translate.Client(api_key)

    # The text to translate
    text = 'Hello, world!'
    # The target language
    target = 'ru'

    # Translates some text into Russian
    translation = translate_client.translate(text, target_language=target)

    print('Text: {}'.format(text))
    print('Translation: {}'.format(
        translation['translatedText'].encode('utf-8')))
    # [END translate_quickstart]


if __name__ == '__main__':
    run_quickstart()
