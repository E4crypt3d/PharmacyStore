# PharmacyStore

PharmacyStore is a web application designed to manage medicine sales for a pharmacy. It provides features for adding sales by staff members, with administrative control over editing, updating, and deleting sales. The admin has the authority to manage user roles, promoting staff members to admin status if needed.

## Features

- **User Roles:**

  - Admins have full control over sales data and user management.
  - Staff members can add sales but cannot edit, update, or delete them.

- **Sales Management:**

  - Staff members can add sales entries.
  - Admins have exclusive rights to edit, update, and delete sales entries.

- **User Management:**

  - Admins can promote staff members to admin status.

- **Sales Analytics:**

  - Total amount of medicine sales.
  - Total amount of medicines in inventory.
  - Performance comparison to the previous month.

- **Bokeh Charts:**

  - Monthly sales representation using Bokeh charts.

- **Sortable Data Table:**
  - Sales data presented in a sortable table for easy analysis.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/E4crypt3d/PharmacyStore.git
   ```

2. Change into the project directory:

   ```bash
   cd PharmacyStore
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python manage.py runserver
   ```

   - The application should be running at `http://localhost:3000`.

## Usage

1. Access the application at http://localhost:3000.
2. Sign in with your credentials.
3. Admins can manage sales, users, and roles.
4. Staff members can add sales.
5. Explore the sales analytics, including total sales, total medicines, and performance comparison.
