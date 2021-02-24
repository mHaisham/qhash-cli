import typer

from qhash.file_hash import generate_file_hash
from typing import Optional

app = typer.Typer()


@app.command()
def qhash(checksum_type: str, file_path: str, compare_with: Optional[str] = typer.Argument(None)):
    typer.echo("")
    checksum = generate_file_hash(checksum_type, file_path)

    if compare_with is None:
        typer.echo(f"\nFile checksum: {typer.style(checksum, fg=typer.colors.GREEN)}\n")
    else:
        fgc = typer.colors.RED

        if checksum == compare_with:
            fgc = typer.colors.GREEN
        typer.echo(f"\nFile checksum: {typer.style(checksum, fg=fgc)}")
        typer.echo(f"Compared with: {typer.style(compare_with, fg=fgc)}\n")


if __name__ == '__main__':
    app()
