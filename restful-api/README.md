### Differences between HTTP and HTTPS

**HTTP (HyperText Transfer Protocol):**
- **Security:** HTTP does not encrypt data being transmitted between the client and server. This means data is sent in plain text, making it vulnerable to eavesdropping and man-in-the-middle attacks.
- **Port:** Typically uses port 80 for communication.
- **Usage:** Suitable for non-sensitive information, like general web browsing where security is not a major concern.

**HTTPS (HyperText Transfer Protocol Secure):**
- **Security:** HTTPS encrypts data using SSL/TLS, making it secure. This prevents unauthorized parties from reading or tampering with the data during transmission.
- **Port:** Typically uses port 443 for communication.
- **Usage:** Essential for transmitting sensitive data such as login information, payment details, and personal information. Commonly used by banking websites, e-commerce sites, and any platform handling personal data.

### Structure of an HTTP Request and Response

**HTTP Request:**
- **Request Line:** Contains the HTTP method, URL path, and HTTP version. For example, `GET /index.html HTTP/1.1`.
- **Headers:** Provide additional information about the request. Common headers include `Host`, `User-Agent`, `Accept`, and `Content-Type`.
- **Body:** (Optional) Contains data sent to the server, typically used with methods like POST or PUT.

**HTTP Response:**
- **Status Line:** Contains the HTTP version, status code, and reason phrase. For example, `HTTP/1.1 200 OK`.
- **Headers:** Provide metadata about the response. Common headers include `Content-Type`, `Content-Length`, `Set-Cookie`, and `Server`.
- **Body:** Contains the requested resource or data.

### Common HTTP Methods

1. **GET:**
   - **Description:** Retrieves data from the server.
   - **Use Case:** Fetching a webpage or data from an API. Example: `GET /home`.

2. **POST:**
   - **Description:** Sends data to the server to create a resource.
   - **Use Case:** Submitting a form or uploading a file. Example: `POST /submit-form`.

3. **PUT:**
   - **Description:** Updates or creates a resource on the server.
   - **Use Case:** Updating user information or replacing a file. Example: `PUT /user/123`.

4. **DELETE:**
   - **Description:** Deletes a resource from the server.
   - **Use Case:** Removing a user account or deleting a post. Example: `DELETE /post/123`.

### Common HTTP Status Codes

1. **200 OK:**
   - **Description:** The request was successful, and the server returned the requested resource.
   - **Scenario:** When a webpage loads successfully.

2. **301 Moved Permanently:**
   - **Description:** The requested resource has been permanently moved to a new URL.
   - **Scenario:** When a webpage has been permanently redirected to a new address.

3. **404 Not Found:**
   - **Description:** The requested resource could not be found on the server.
   - **Scenario:** When a user tries to access a non-existent page.

4. **500 Internal Server Error:**
   - **Description:** The server encountered an unexpected condition that prevented it from fulfilling the request.
   - **Scenario:** When there is a bug or issue in the server code.

5. **403 Forbidden:**
   - **Description:** The server understood the request but refuses to authorize it.
   - **Scenario:** When a user tries to access a restricted page without proper permissions.
