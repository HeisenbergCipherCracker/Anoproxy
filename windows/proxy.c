#include <stdio.h>
#include <winsock2.h>

int main() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("WSAStartup failed\n");
        return 1;
    }

    // Create a socket
    SOCKET clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == INVALID_SOCKET) {
        printf("Socket creation failed\n");
        WSACleanup();
        return 1;
    }

    // Set up proxy server details (replace ProxyPort with your proxy port)
    int ProxyPort = 8080; // Replace with your proxy port
    struct sockaddr_in proxyServer;
    proxyServer.sin_family = AF_INET;
    proxyServer.sin_port = htons(ProxyPort); // Replace with your proxy port
    proxyServer.sin_addr.s_addr = inet_addr("159.192.139.178"); // Replace with your proxy IP address

    // Connect to the proxy server
    if (connect(clientSocket, (struct sockaddr*)&proxyServer, sizeof(proxyServer)) == SOCKET_ERROR) {
        printf("Proxy server connection failed\n");
        closesocket(clientSocket);
        WSACleanup();
        return 1;
    }

    // Display a success message
    printf("Connected to the proxy server successfully\n");

    // Send an HTTP GET request (modify as needed)
    const char* getRequest = "GET http://example.com HTTP/1.1\r\n\r\n";
    send(clientSocket, getRequest, strlen(getRequest), 0);

    // Receive and process the response (not shown in this example)

    // Cleanup and close the socket
    closesocket(clientSocket);
    WSACleanup();

    return 0;
}
