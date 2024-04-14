import semantic_release
import git


class MyParserOptions(semantic_release.ParserOptions): ...


class MyCommitParser(
    semantic_release.CommitParser[semantic_release.ParseResult, MyParserOptions]
):
    parser_options = MyParserOptions

    def parse(self, commit: git.objects.commit.Commit) -> semantic_release.ParseResult:
        return semantic_release.ParsedCommit(
            bump=semantic_release.LevelBump.PATCH,
            type="patch",
            scope="scope",
            descriptions=["descriptions"],
            breaking_descriptions=["breaking_descriptions"],
            commit=commit
        )
