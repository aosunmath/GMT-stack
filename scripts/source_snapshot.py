"""Fingerprint an explicitly registered local manuscript without claiming a Git revision."""
from hashlib import sha256
import json
from pathlib import Path


def manuscript_snapshot(directory):
    directory = Path(directory).resolve()
    if not directory.is_dir():
        raise ValueError('Missing local manuscript directory')
    files = {}
    for path in sorted(directory.rglob('*')):
        if path.is_symlink():
            raise ValueError('Local manuscripts must not contain symbolic links')
        if path.is_file():
            files[path.relative_to(directory).as_posix()] = sha256(path.read_bytes()).hexdigest()
    if 'book.tex' not in files or 'references.bib' not in files:
        raise ValueError('Local manuscripts require book.tex and references.bib')
    digest = sha256(json.dumps(files, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return {'kind': 'local-manuscript', 'source_sha256': digest, 'files': files}


def revision_id(edition):
    return edition.get('commit') or 'sha256:' + edition['source_sha256']


def revision_markup(edition, repository):
    from html import escape
    if edition.get('kind') == 'local-manuscript':
        return 'Manuscript snapshot SHA-256 <code>' + edition['source_sha256'][:16] + '</code>. This identifies the exact local source files used for this build.'
    commit = edition['commit']
    return f'<a href="{escape(repository)}/commit/{commit}">Source revision {commit[:12]} ↗</a>'
