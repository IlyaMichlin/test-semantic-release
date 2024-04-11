from typing import Any

import semantic_release
import git


class MyParserOptions(semantic_release.ParserOptions):
    def __init__(self, message_prefix: str, **_: Any) -> None:
        super().__init__(**_)
        self.prefix = message_prefix * 2


class MyCommitParser(
    semantic_release.CommitParser[semantic_release.ParseResult, MyParserOptions]
):
    def parse(self, commit: git.objects.commit.Commit) -> semantic_release.ParseResult:
        print("commit.message: ", commit.message)
        return semantic_release.ParsedCommit(
            bump=semantic_release.LevelBump.PATCH,
            type="feat",
            scope="",
            descriptions=[""],
            breaking_descriptions=[""],
            commit=commit
        )
