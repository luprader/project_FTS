# Project Financial  time series

Authors:
[Albin Essman](https://github.com/AlbinEssman),
[Lukas Prader](https://github.com/luprader),
[Noah Tingbratt](https://github.com/noahtingb),
[Tom Xu](https://github.com/tommingyuanxu2002-png),
[Truls Levenstam](https://github.com/Trulslevenstam),
[Yangguang Chen](https://github.com/YgggC)

This project contains the code used to create the results of group 7 in the course "Financial time series" at Chalmers / University of Gothenburg 2026.

To run the project, set it up with uv and put the dataset "spiff_data-2.csv" into the project root.
Tasks should be run in order, since there are some dependencies on generated output files.

## Project setup and management with uv
https://docs.astral.sh/uv/

### Install uv
```bash
pipx install uv==0.9.5
```

### Sync (install) project dependencies
```bash
uv sync
```

Run the files either using "uv run" or select the virtual environment kernel in the notebooks directly and run as usual.