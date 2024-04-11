import semantic_release
import git


class MyParserOptions(semantic_release.ParserOptions): ...


class MyCommitParser(
    semantic_release.CommitParser[semantic_release.ParseResult, MyParserOptions]
):
    parser_options = MyParserOptions

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
