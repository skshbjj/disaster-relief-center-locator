# Disaster Relief Center Locator

A web application to locate and display relief centers providing essential resources like food, water, medical aid, and shelter. This project integrates a React-based frontend with a Flask backend, utilizing Elasticsearch for geospatial data storage and querying.

## Features

- Interactive map to visualize relief center locations.
- Ability to filter relief centers by resource type (food, water, medical aid, shelter).
- Search within a customizable radius and location.
- Automatically detects and displays the user's current location on the map.
- Data powered by Elasticsearch for real-time querying.

---
## Screenshots
### Current Location and Search Feature
![Current Location and Search Feature](images/ss1.jpg)

### Relief Center Information
![Relief Center Information](images/ss2.jpg)




## Setup Instructions

### Prerequisites

- Python 3.7+ for the backend.
- Node.js 16+ and npm for the frontend.
- Elasticsearch (Cloud or Local instance).
- Basic knowledge of React and Flask.

---

## Backend Setup

### Navigate to the Project Root

```bash
cd backend
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Update Elasticsearch Credentials

Update `app.py` with your Elasticsearch credentials and Elastic Cloud URL if necessary.

### Run the Flask Server

Start the backend server:

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`.

---

## Frontend Setup

### Navigate to the Frontend Directory

```bash
cd relief-locator-frontend
```

### Install Dependencies

Install the required frontend packages:

```bash
npm install
```

### Update Environment Variables

In the `.env` file (located in `relief-locator-frontend`), set the backend URL:

```env
REACT_APP_BACKEND_URL=http://127.0.0.1:5000
```

### Start the Development Server

Start the React development server:

```bash
npm start
```

The frontend will be accessible at `http://127.0.0.1:3000`.

---

## Usage

1. Open the frontend at `http://127.0.0.1:3000`.
2. Use the dropdown and search bar to filter relief centers by resource type and radius.
3. View markers for each relief center on the map, including details like name, resources, address, and contact.
4. Use the "Use My Location" button to center the map on your current location and search within a radius.

---

## Authors

- **Sakshi Bajaj** - [GitHub Profile](https://github.com/skshbjj)

Feel free to reach out for any questions or suggestions!


## License

This project is open-source and available under the MIT License.
