import typer
import file_hash as f

app = typer.Typer()


@app.command()
def qhash(checksum_type: str, file_path: str):
    output = f.generate_file_hash(checksum_type, file_path)
    print(output)


if __name__ == '__main__':
    app()
