# Blogging_Platform_API

## Blog API Documentation

### API Endpoints
1. **Create Blog**  
   - **Path**: `/create/`  
   - **Method**: POST  
   - **View**: `BlogCreateView`  
   - **Description**: Creates a new blog post.  
   - **Request**:  
     ```json
     {"title": "My First Blog", "content": "This is the content of my first blog post.", "category": "General"}
     ```  
   - **Response**:  
     ```json
     {"id": 1, "title": "My First Blog", "content": "This is the content of my first blog post.", "category": "General", "created_at": "2024-12-28T20:51:47+02:00"}
     ```  

2. **Update Blog**  
   - **Path**: `/update/<int:id>/`  
   - **Method**: PUT/PATCH  
   - **View**: `BlogUpdateView`  
   - **Description**: Updates an existing blog post identified by `id`.  
   - **Request**:  
     ```json
     {"title": "Updated Blog Title", "content": "Updated content for the blog post."}
     ```  
   - **Response**:  
     ```json
     {"id": 1, "title": "Updated Blog Title", "content": "Updated content for the blog post.", "category": "General", "updated_at": "2024-12-28T20:51:47+02:00"}
     ```  

3. **Delete Blog**  
   - **Path**: `/delete/<int:id>/`  
   - **Method**: DELETE  
   - **View**: `BlogDeleteView`  
   - **Description**: Deletes a blog post identified by `id`.  
   - **Response**:  
     ```json
     {"message": "Blog post deleted successfully."}
     ```  

4. **Get Blog Detail**  
   - **Path**: `/detail/<int:id>/`  
   - **Method**: GET  
   - **View**: `BlogDetailView`  
   - **Description**: Retrieves details of a blog post identified by `id`.  
   - **Response**:  
     ```json
     {"id": 1, "title": "My First Blog", "content": "This is the content of my first blog post.", "category": "General", "created_at": "2024-12-28T20:51:47+02:00"}
     ```  

5. **Create Category**  
   - **Path**: `/category/create/`  
   - **Method**: POST  
   - **View**: `CategoryCreateView`  
   - **Description**: Creates a new category.  

6. **Search Blogs**  
   - **Path**: `/search/`  
   - **Method**: GET  
   - **View**: `SearchView`  
   - **Description**: Searches for blogs based on query parameters.  

7. **Filter Blogs**  
   - **Path**: `/filter/`  
   - **Method**: GET  
   - **View**: `BlogFilterationView`  
   - **Description**: Filters blogs based on specified criteria.  

8. **List Blogs**  
   - **Path**: `/list/`  
   - **Method**: GET  
   - **View**: `BlogListView`  
   - **Description**: Lists all blog posts.  
   - **Response**:  
     ```json
     [{"id": 1, "title": "My First Blog", "created_at": "2024-12-28T20:51:47+02:00"}, {"id": 2, "title": "Another Blog", "created_at": "2024-12-28T20:51:47+02:00"}]
     ```  

9. **Delete Tag**  
   - **Path**: `/tag/delete/<int:id>/`  
   - **Method**: DELETE  
   - **View**: `TagDeleteView`  
   - **Description**: Deletes a tag identified by `id`.  

### Accounts API Documentation

### API Endpoints
1. **User Registration**  
   - **Path**: `/register/`  
   - **Method**: POST  
   - **View**: `UserRegisterView`  
   - **Description**: Registers a new user.  
   - **Request**:  
     ```json
     {"username": "newuser", "password": "securepassword", "email": "user@example.com"}
     ```  
   - **Response**:  
     ```json
     {"id": 1, "username": "newuser", "email": "user@example.com"}
     ```  

2. **User Login**  
   - **Path**: `/login/`  
   - **Method**: POST  
   - **View**: `UserLoginView`  
   - **Description**: Logs in a user and returns authentication tokens.  
   - **Request**:  
     ```json
     {"username": "newuser", "password": "securepassword"}
     ```  
   - **Response**:  
     ```json
     {"token": "your_auth_token_here"}
     ```  

3. **Get Users**  (for admin only) 
   - **Path**: `/users/`  
   - **Method**: GET  
   - **View**: `UserView`  
   - **Description**: Retrieves a list of users (excluding staff).  
   - **Response**:  
     ```json
     [{"id": 1, "username": "user1", "email": "user1@example.com"}, {"id": 2, "username": "user2", "email": "user2@example.com"}]
     ```  

4. **Update Profile**  
   - **Path**: `/profile/update/`  
   - **Method**: PUT  
   - **View**: `UpdateProfileView`  
   - **Description**: Updates the authenticated user's profile.  
   - **Request**:  
     ```json
     {"email": "updateduser@example.com"}
     ```  
   - **Response**:  
     ```json
     {"id": 1, "username": "newuser", "email": "updateduser@example.com"}
     ```  

5. **User Logout**  
   - **Path**: `/logout/`  
   - **Method**: POST  
   - **View**: `UserLogoutView`  
   - **Description**: Logs out the authenticated user.  
   - **Response**:  
     ```json
     {"message": "Logout successful."}
     ```  
