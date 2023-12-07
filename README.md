# Sort-Algorithms
implement high efficient sorting algoritms 
- merge sort
- quick sort

# Setup Python Environment
- Creating an environment from the environment.yml file <br/>
`conda env create -f environment.yml -n "sorting_algo"`
- Activate env <br/>
`conda activate sorting_algo`
- Export your active environment to a new file <br/>
`conda env export > environment.yml`

# How to Run 
- Go to the location where `main.py` is <br/>
`python -m main`
# How to Run Test Cases
- Go to the project root dir <br/>
`python -m pytest` <br/>
`python -m pytest -v --cov ./src/` 


