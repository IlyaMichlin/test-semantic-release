from semantic_release import ParsedCommit, LevelBump, ParserOptions, CommitParser, ParseResult
import git


class MyParserOptions(ParserOptions): ...


class MyCommitParser(
    CommitParser[ParseResult, MyParserOptions]
):
    parser_options = MyParserOptions

    def parse(self, commit: git.objects.commit.Commit) -> ParseResult:
        return ParsedCommit(
            bump=LevelBump.PATCH,
            type="patch",
            scope="",
            descriptions=[""],
            breaking_descriptions=[""],
            commit=commit
        )
