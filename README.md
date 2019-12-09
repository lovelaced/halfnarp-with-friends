# halfnarp-with-friends
 A python 3 script to help you group up with friends for talks based on your halfnarp submissions.
 Also can be used to retrieve a text list of the titles of talks you're attending.

Configuration: edit `consolidate_talks.py` to add your halfnarp string found in the URL of your completed halfnarp:

```python
friend_ids = {
              "your_name":'your unique halfnarp string',
              "your_friend":'their unique halfnarp string',
              "ccc_buddy":'and so on'
              }
```

Usage: `python consolidate_talks.py`

*Will only show talks that more than one person is attending.*
