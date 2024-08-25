## Permissions and Groups Setup

### Permissions
- `can_view`: Allows viewing of Book instances.
- `can_create`: Allows creating of new Book instances.
- `can_edit`: Allows editing of existing Book instances.
- `can_delete`: Allows deletion of Book instances.

### Groups
- `Editors`: Can create and edit books.
- `Viewers`: Can view books.
- `Admins`: Can view, create, edit, and delete books.

### Views
- `book_list`: Requires `can_view` permission.
- `book_edit`: Requires `can_edit` permission.

Ensure that users are assigned to the correct groups to perform actions within the application.