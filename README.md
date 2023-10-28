# Automatic Program Repair

## Testing dataset

### Running tests
To run one test file just locate yourself on the root of the repository and execute:

```cmd
pytest .\tests\test_t2p1.py
```

### Using custom import strategy
To test the dataset it was necessary implement a custom [import strategy](./tests/import_utils.py), which enable importing functions without executing the top level statements of the script (those that are not in `if __name__ == '__main__'`).

To create more similar test you could just call `import_function` with the *`<function_name_to_import>`* and the *`<function_file_path>`*. The call returns the function object (callable) that you specify.