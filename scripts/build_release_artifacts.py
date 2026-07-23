#!/usr/bin/env python3
"""Build deterministic release archives and the repository SHA-256 manifest."""

from __future__ import annotations

import gzip
import hashlib
import io
from pathlib import Path
import tarfile


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = "v1.0.2"
PREFIX = f"semilocal-reflected-packet-oscillation-{VERSION}"
PAPER_VERSION = "v1.0.0"
PAPER_PREFIX = (
    f"semilocal-reflected-packet-oscillation-paper-{PAPER_VERSION}"
)


def regular_files(paths: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_file():
            files.add(path)
        elif path.is_dir():
            files.update(
                item
                for item in path.rglob("*")
                if item.is_file()
                and "__pycache__" not in item.parts
                and item.suffix not in {".pyc", ".pyo"}
                and item.name != ".DS_Store"
            )
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def archive(name: str, files: list[Path], prefix: str = PREFIX) -> Path:
    destination = DIST / name
    tar_buffer = io.BytesIO()
    with tarfile.open(fileobj=tar_buffer, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for path in files:
            relative = path.relative_to(ROOT)
            data = path.read_bytes()
            info = tarfile.TarInfo(
                name=f"{prefix}/{relative.as_posix()}"
            )
            info.size = len(data)
            info.mtime = 0
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            info.mode = 0o755 if path.suffix == ".py" else 0o644
            tar.addfile(info, io.BytesIO(data))
    with destination.open("wb") as handle:
        with gzip.GzipFile(
            filename="",
            mode="wb",
            fileobj=handle,
            mtime=0,
            compresslevel=9,
        ) as compressed:
            compressed.write(tar_buffer.getvalue())
    return destination


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)

    latex_files = regular_files(
        [ROOT / "paper" / "main.tex", ROOT / "paper" / "sections"]
    )
    code_certificate_files = regular_files(
        [
            ROOT / "code",
            ROOT / "tests",
            ROOT / "certificates",
            ROOT / "requirements.txt",
            ROOT / "REPRODUCIBILITY.md",
        ]
    )
    full_source_files = regular_files(
        [
            ROOT / "README.md",
            ROOT / "REPRODUCIBILITY.md",
            ROOT / "ZENODO.md",
            ROOT / "CITATION.cff",
            ROOT / "NOTICE",
            ROOT / "requirements.txt",
            ROOT / ".gitignore",
            ROOT / ".github",
            ROOT / "paper" / "main.tex",
            ROOT / "paper" / "sections",
            ROOT / "research",
            ROOT / "code",
            ROOT / "tests",
            ROOT / "certificates",
            ROOT / "scripts",
        ]
    )
    paper_reproducibility_files = regular_files(
        [
            ROOT / "README.md",
            ROOT / "REPRODUCIBILITY.md",
            ROOT / "ZENODO.md",
            ROOT / "CITATION.cff",
            ROOT / "NOTICE",
            ROOT / "requirements.txt",
            ROOT / ".gitignore",
            ROOT / ".github",
            ROOT / "research",
            ROOT / "code",
            ROOT / "tests",
            ROOT / "certificates",
            ROOT / "scripts",
        ]
    )

    release_assets = [
        archive(f"{PREFIX}-latex-source.tar.gz", latex_files),
        archive(
            f"{PREFIX}-code-certificates.tar.gz",
            code_certificate_files,
        ),
        archive(f"{PREFIX}-source.tar.gz", full_source_files),
    ]
    paper_pdf = DIST / f"{PAPER_PREFIX}.pdf"
    paper_pdf.write_bytes((ROOT / "paper" / "main.pdf").read_bytes())
    zenodo_assets = [
        paper_pdf,
        archive(
            f"{PAPER_PREFIX}-sources.tar.gz",
            latex_files,
            prefix=PAPER_PREFIX,
        ),
        archive(
            f"{PAPER_PREFIX}-reproducibility.tar.gz",
            paper_reproducibility_files,
            prefix=PAPER_PREFIX,
        ),
    ]
    zenodo_manifest = ROOT / "ZENODO_UPLOAD_SHA256SUMS"
    zenodo_manifest.write_text(
        "\n".join(
            f"{sha256(path)}  {path.name}" for path in zenodo_assets
        )
        + "\n",
        encoding="utf-8",
    )
    zenodo_assets.append(zenodo_manifest)
    release_assets.extend(zenodo_assets)

    manifest_paths = regular_files(
        [
            ROOT / "README.md",
            ROOT / "REPRODUCIBILITY.md",
            ROOT / "ZENODO.md",
            ROOT / "ZENODO_UPLOAD_SHA256SUMS",
            ROOT / "CITATION.cff",
            ROOT / "NOTICE",
            ROOT / "requirements.txt",
            ROOT / ".github",
            ROOT / "paper",
            ROOT / "research",
            ROOT / "code",
            ROOT / "tests",
            ROOT / "certificates",
            ROOT / "scripts",
        ]
    )
    manifest_paths = [
        path
        for path in manifest_paths
        if path.name != "SHA256SUMS" and "__pycache__" not in path.parts
    ]
    manifest_paths.extend(release_assets)
    manifest_paths = sorted(
        set(manifest_paths), key=lambda item: item.relative_to(ROOT).as_posix()
    )

    lines = [
        f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}"
        for path in manifest_paths
    ]
    (ROOT / "SHA256SUMS").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    for path in release_assets:
        print(f"{sha256(path)}  {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
