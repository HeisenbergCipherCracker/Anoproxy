#include <iostream>
#include <sqlite3.h>
#include <fstream>

// Callback function to process query results
int callback(void* data, int argc, char** argv, char** azColName) {
    std::ofstream outFile("output.txt", std::ios::app); // Open the output file for appending
    if (!outFile.is_open()) {
        std::cerr << "Failed to open output file." << std::endl;
        return 1;
    }

    for (int i = 0; i < argc; i++) {
        std::cout << azColName[i] << ": " << (argv[i] ? argv[i] : "NULL") << std::endl;
        outFile << azColName[i] << ": " << (argv[i] ? argv[i] : "NULL") << std::endl;
    }
    std::cout << std::endl;
    outFile << std::endl;

    outFile.close();
    return 0;
}

void retrieveData() {
    sqlite3* db;
    int rc = sqlite3_open("your_database.db", &db);
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to open database: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    const char* sql = "SELECT * FROM proxies;";
    char* errMsg;
    rc = sqlite3_exec(db, sql, callback, 0, &errMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to execute statement: " << errMsg << std::endl;
        sqlite3_free(errMsg);
        sqlite3_close(db);
        return;
    }

    sqlite3_close(db);
}

int main() {
    // Open the database
    sqlite3* db;
    int rc = sqlite3_open("your_database.db", &db);
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to open database: " << sqlite3_errmsg(db) << std::endl;
        return 1;
    }

    // Create the table (if not exists)
    const char* createTableSQL = "CREATE TABLE IF NOT EXISTS proxies ("
                                 "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                 "ip_address TEXT,"
                                 "port INTEGER,"
                                 "country_city TEXT,"
                                 "speed INTEGER,"
                                 "type TEXT,"
                                 "level_of_anonymity TEXT);";
    char* errMsg;
    rc = sqlite3_exec(db, createTableSQL, 0, 0, &errMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to create table: " << errMsg << std::endl;
        sqlite3_free(errMsg);
        sqlite3_close(db);
        return 1;
    }

    // Retrieve and print data
    retrieveData();

    // Insert new data
    const char* insertSQL = "INSERT INTO proxies (ip_address, port, country_city, speed, type, level_of_anonymity) "
                            "VALUES (?, ?, ?, ?, ?, ?);";
    sqlite3_stmt* stmt;
    rc = sqlite3_prepare_v2(db, insertSQL, -1, &stmt, 0);
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        sqlite3_close(db);
        return 1;
    }

    auto insertData = [&](const char* ipAddress, int port, const char* countryCity, int speed,
                          const char* type, const char* levelOfAnonymity) {
        rc = sqlite3_bind_text(stmt, 1, ipAddress, -1, SQLITE_STATIC);
        rc = sqlite3_bind_int(stmt, 2, port);
        rc = sqlite3_bind_text(stmt, 3, countryCity, -1, SQLITE_STATIC);
        rc = sqlite3_bind_int(stmt, 4, speed);
        rc = sqlite3_bind_text(stmt, 5, type, -1, SQLITE_STATIC);
        rc = sqlite3_bind_text(stmt, 6, levelOfAnonymity, -1, SQLITE_STATIC);

        rc = sqlite3_step(stmt);
        if (rc != SQLITE_DONE) {
            std::cerr << "Failed to execute statement: " << sqlite3_errmsg(db) << std::endl;
        }

        rc = sqlite3_reset(stmt);
        if (rc != SQLITE_OK) {
            std::cerr << "Failed to reset statement: " << sqlite3_errmsg(db) << std::endl;
        }
    };

    insertData("145.239.85.58", 9300, "Poland", 500, "SOCKS4, SOCKS5", "High");
    insertData("46.4.96.137", 1080, "Germany", 580, "SOCKS5", "High");
    insertData("47.91.88.100", 1080, "Germany \"Frankfurt am Main\"", 260, "SOCKS5", "High");

    // Finalize and close the database
    sqlite3_finalize(stmt);
    sqlite3_close(db);

    return 0;
}

