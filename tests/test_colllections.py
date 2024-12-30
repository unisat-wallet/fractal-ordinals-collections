# -*- coding: utf-8 -*-
import os
import json

COLLECTIONS = "./collections"


def test_home_structure():
    expected_directories = [
        "LICENSE",
        "requirements.txt",
        ".pytest_cache",
        "tests",
        "README.md",
        "env",
        ".gitignore",
        ".git",
        "collections",
        ".circleci",
        "notebooks",
        "scripts",
        ".DS_Store",
    ]
    current_directories = os.listdir()
    correct_directories = [x in expected_directories for x in current_directories]
    assert all(correct_directories), "Top level changes are not allowed"


def test_collections_structure():
    current_collections = os.listdir(COLLECTIONS)
    current_collections = [x for x in current_collections if x != ".DS_Store"]
    folders = [not os.path.isfile("{}/{}".format(COLLECTIONS, x)) for x in current_collections]
    assert all(folders), "Invalid structure, include your files in a nested directory"


def test_meta():
    expected_meta = {
        "name": "Based Apes",
        "inscription_icon": "159f5b1437375424ba798c92f10670f19baf3e5d10be3bf5fbd4d4a50cf642ddi0",
        "supply": "100",
        "slug": "based-apes",
        "description": "",
        "twitter_link": "https://x.com/BasedApes",
        "discord_link": "https://discord.com/invite/ordinalswallet",
        "website_link": "",
    }
    current_collections = os.listdir(COLLECTIONS)
    current_collections = [x for x in current_collections if x != ".DS_Store"]

    for x in current_collections:
        with open("{}/{}/meta.json".format(COLLECTIONS, x), "r", encoding="utf-8") as file:
            meta = json.load(file)

        assert set(meta.keys()) == set(expected_meta.keys()), "Invalid meta data keys"

        for y in zip(meta.values(), meta.keys()):
            assert isinstance(y[0], str), "Invalid data type, use a string"
            if y[1].endswith("link"):
                if y[0]:
                    assert y[0].startswith("https://") or y[0].startswith("http://"), "link must start with https://"

        assert (len(meta.get("inscription_icon")) == 66) or meta.get("inscription_icon"), "Invalid inscription Id"
        assert meta.get("slug").lower() == meta.get("slug"), "Slug must be lowercase"
        assert len(meta.get("name")) <= 60, "Name is too long"
        assert len(meta.get("slug")) < 60, "Slug is too long"
        assert meta.get("slug") == x, "Slug does not match directory name"


def ishex(s):
    try:
        n = int(s, 16)
        return True
    except ValueError:
        return False


def test_inscriptions():
    current_collections = os.listdir(COLLECTIONS)
    current_collections = [x for x in current_collections if x != ".DS_Store"]
    for x in current_collections:
        with open("{}/{}/inscriptions.json".format(COLLECTIONS, x), "r", encoding="utf-8") as file:
            inscriptions = json.load(file)
        for y in inscriptions:
            assert y.get("id")
            assert y.get("meta")
            assert y.get("attributes") is None, "Attributes belong in meta object"
            if y.get("meta").get("attributes"):
                for a in y.get("meta").get("attributes"):
                    if x not in ["ordinal-gen1-pokemon", "bitcoin-jpgs"]:
                        assert "trait_type" in a, "Attribute must have trait type"
                        assert "value" in a, "Attribute must have trait value"
            assert len(y.get("id").strip()) == 66
            assert ishex(y.get("id")[0:64]), "inscription ids must be valid hex"
            assert isinstance(y.get("meta").get("name"), str)


def test_uniqueness():
    input_collections = os.listdir(COLLECTIONS)
    input_collections = [x for x in input_collections if x != ".DS_Store"]
    print("\n\n")

    # add new collections
    all_inscription_ids = []
    for collection in input_collections:
        print(collection)
        if collection in ["<1k", "<10k", "<100k", "unisat-names"]:
            continue
        with open("{}/{}/inscriptions.json".format(COLLECTIONS, collection), "r", encoding="utf-8") as file:
            inscriptions = json.load(file)
        inscription_ids = []
        for x in inscriptions:
            inscription_ids.append(x.get("id"))
        all_inscription_ids = all_inscription_ids + inscription_ids
        duplicates = len(all_inscription_ids) - len(set(all_inscription_ids))
        assert duplicates == 0
