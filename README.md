# PersonaMatrix A Fake Identity Generator

This Python-based tool generates realistic user data intended for use when registering on new services, Protect your privacy by generating fictional identities for online registrations, sign-ups, and subscriptions Starting with German data, the project is structured for easy expansion to include datasets from other countries and cultures, serving privacy-conscious users globally.
<p align="center">
<img src="https://cdn.idcreator.com/media/sc/id-card-templates/drone_pilots_license_2_featured.png" height="300">
</p>

## Main Features

- Generates comprehensive and realistic user profiles to protect users' privacy during service registration.
- Customizable data generation including names, addresses, email, phone numbers, birthdays, ages, usernames, passwords, and user agent strings.
- Initial support for German data, with a modular design for straightforward addition of other regions' data sets.
- Facilitates the safeguarding of personal information by providing alternative, plausible data for online forms.

## Installation

Ensure Python 3.x is installed on your system. The project relies on the `fake-useragent` library among potentially others. Install all necessary libraries using the `requirements.txt` file included in the project:

```bash
pip install -r requirements.txt
```

## Usage

To generate a user profile, run the `main.py` script. This script utilizes datasets located in the `data` directory. Modify or augment these datasets to customize the generated data:

```bash
python main.py
```

Your project directory should be structured as follows, including the initial datasets and any additions:

```
project/
│
├── main.py
├── requirements.txt
└── data/
    └── german/
        ├── first-names.txt
        ├── last-names.txt
        ├── streets.txt
        ├── cities.txt
        ├── zip-codes.txt
        └── mobile-numbers.txt
```

## Contributions

Contributions that extend the dataset, enhance functionality, or improve the project's privacy protection capabilities are welcome. To add data from additional countries or regions, create a new directory within `data/` and populate it with `.txt` files relevant to each category of data (e.g., `first-names.txt`, `last-names.txt`).

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE.md) file for more details.

## Acknowledgments

- Utilizes the `fake-useragent` library to generate realistic user agent strings. ([fake-useragent/fake-useragent](https://github.com/fake-useragent/fake-useragent))
- German data sets were partly sourced from [oliverpitsch/craft-data-german](https://github.com/oliverpitsch/craft-data-german) repository.
