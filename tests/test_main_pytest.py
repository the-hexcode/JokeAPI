import os
import time
import pytest
from dotenv import load_dotenv
from jokeapi import Jokes

load_dotenv()
TOKEN = os.getenv("token")

@pytest.fixture(scope="module")
def jokes():
    return Jokes()

# Basic joke retrieval
@pytest.mark.timeout(2)
def test_get_joke_basic(jokes):
    resp = jokes.get_joke()
    assert resp, "Expected non-empty joke response"

# Auth token (skipped if no token)
@pytest.mark.timeout(2)
# @pytest.mark.skipif(not TOKEN, reason="No auth token in environment")
def test_get_joke_with_auth(jokes):
    resp = jokes.get_joke(auth_token=TOKEN)
    assert resp, "Expected response when using auth token"

# Categories
@pytest.mark.parametrize("category", ["programming", "misc", "dark"]) 
@pytest.mark.timeout(2)
# @pytest.mark.skipif(not TOKEN, reason="No auth token in environment")
def test_categories(jokes, category):
    resp = jokes.get_joke(category=[category], auth_token=TOKEN)
    assert resp, f"Expected response for category {category}"
    time.sleep(1)

# Blacklist flags
@pytest.mark.parametrize("flag", ["nsfw", "religious", "political", "racist", "sexist"]) 
@pytest.mark.timeout(2)
# @pytest.mark.skipif(not TOKEN, reason="No auth token in environment")
def test_blacklist_flags(jokes, flag):
    resp = jokes.get_joke(blacklist=[flag], auth_token=TOKEN)
    assert resp, f"Expected response when blacklisting {flag}"
    time.sleep(1)

# Response formats (json covered above). xml / yaml rely on API structure.
@pytest.mark.parametrize("fmt", ["xml", "yaml"]) 
@pytest.mark.timeout(2)
# @pytest.mark.skipif(not TOKEN, reason="No auth token in environment")
def test_response_formats(jokes, fmt):
    resp = jokes.get_joke(response_format=fmt, auth_token=TOKEN)
    assert resp, f"Expected response for format {fmt}"
    time.sleep(1)

# Types
@pytest.mark.parametrize("jtype", ["single", "twopart"]) 
@pytest.mark.timeout(2)
# @pytest.mark.skipif(not TOKEN, reason="No auth token in environment")
def test_joke_types(jokes, jtype):
    resp = jokes.get_joke(type=jtype, auth_token=TOKEN)
    assert resp, f"Expected response for type {jtype}"
    time.sleep(1)

# Search string
@pytest.mark.timeout(2)
# @pytest.mark.skipif(not TOKEN, reason="No auth token in environment")
def test_search_string(jokes):
    resp = jokes.get_joke(search_string="search", auth_token=TOKEN)
    assert resp, "Expected response for search string query"

# ID range (pick a modest range)
@pytest.mark.timeout(2)
# @pytest.mark.skipif(not TOKEN, reason="No auth token in environment")
def test_id_range(jokes):
    resp = jokes.get_joke(id_range=[30, 151], auth_token=TOKEN)
    assert resp, "Expected response for id range"

# Negative tests mirroring validation logic
@pytest.mark.timeout(5)
def test_invalid_category_raises(jokes):
    with pytest.raises(ValueError):
        jokes.get_joke(category=["not_a_real_category"])  # invalid

@pytest.mark.timeout(5)
def test_invalid_response_format_raises(jokes):
    with pytest.raises(Exception):
        jokes.get_joke(response_format="invalidfmt")

@pytest.mark.timeout(5)
def test_invalid_type_raises(jokes):
    with pytest.raises(ValueError):
        jokes.get_joke(type="notatype")

@pytest.mark.timeout(5)
def test_invalid_id_range_length_raises(jokes):
    with pytest.raises(ValueError):
        jokes.get_joke(id_range=[0,1,2])

@pytest.mark.timeout(5)
def test_invalid_id_range_negative_start_raises(jokes):
    with pytest.raises(ValueError):
        jokes.get_joke(id_range=[-1,10])
