#include <iostream>
#include <string>
#include <fstream>
#include <filesystem>
using namespace std;

int getValidNumber()
{
    int x;

    while (!(cin >> x))
    {
        cin.clear();
        cin.ignore(1000, '\n');
        cout << "Invalid input. Please enter a number: ";
    }

    return x;
}

class Movie
{

private:
    string title;
    string genre;
    double basePrice;

public:
    Movie()
    {
        title = "";
        genre = "";
        basePrice = 0;
    }
    Movie(string t, string g, double p)
    {
        title = t;
        genre = g;
        basePrice = p;
    }

    void set_title()
    {
        getline(cin, title);
    }
    void set_genre()
    {
        cin >> genre;
    }
    void set_basePrice()
    {
        while (!(cin >> basePrice)) 
        {
            cin.clear();
            cin.ignore(1000, '\n');
            cout << "Invalid input. Please enter a valid number for the price: ";
        }
    }

    string get_title()
    {
        return title;
    }
    string get_genre()
    {
        return genre;
    }
    double get_basePrice()
    {
        return basePrice;
    }
};

class Seat
{

protected:
    int row;
    int coloumn;
    bool isBooked;

public:
    Seat(int r, int col)
    {
        row = r;
        coloumn = col;
        isBooked = false;
    }

    virtual ~Seat() {}

    void bookSeat()
    {
        isBooked = true;
    }
    void cancelSeat()
    {
        isBooked = false;
    }
    bool isAvailable()
    {
        return !isBooked;
    }

    virtual double calculatePrice(double basePrice) const = 0;
};

class Regular_Seat : public Seat
{
public:
    Regular_Seat(int r, int col) : Seat(r, col) {}
    double calculatePrice(double basePrice) const override { return basePrice; }
};

class VIP_Seat : public Seat
{
public:
    VIP_Seat(int r, int col) : Seat(r, col) {}
    double calculatePrice(double basePrice) const override { return basePrice * 1.4; }
};

class AdminManager
{
private:
    string password;
    int movieCount;
    const string moviesFile = "movies.txt";

    void saveMoviesToFile()
    {
        ofstream outFile(moviesFile);
        if (!outFile.is_open())
        {
            cout << "\n[!] Failed to save movies to file.\n";
            return;
        }

        for (int i = 0; i < movieCount; i++)
        {
            outFile << moviesList[i].get_title() << '|' << moviesList[i].get_genre() << '|' << moviesList[i].get_basePrice() << '\n';
        }

        outFile.close();
    }

    void loadMoviesFromFile()
    {
        ifstream inFile(moviesFile);
        if (!inFile.is_open())
        {
            return;
        }

        movieCount = 0;
        string line;
        while (getline(inFile, line) && movieCount < 10)
        {
            size_t first = line.find('|');
            size_t second = line.find('|', first == string::npos ? string::npos : first + 1);
            if (first == string::npos || second == string::npos)
            {
                continue;
            }

            string title = line.substr(0, first);
            string genre = line.substr(first + 1, second - first - 1);
            double price = stod(line.substr(second + 1));

            moviesList[movieCount] = Movie(title, genre, price);
            movieCount++;
        }

        inFile.close();
    }

public:
    Movie moviesList[10];

    AdminManager()
    {
        password = "1234";
        movieCount = 0;
        loadMoviesFromFile();
    }

    bool login()
    {
        string inputPass;
        cout << "\n[Security] Enter Admin Password: ";
        cin >> inputPass;
        return (inputPass == password);
    }

    int getMovieCount()
    {
        return movieCount;
    }

    void addMovie()
    {
        if (movieCount < 10)
        {

            cout << "Enter Movie Title: ";
            cin.ignore(1000, '\n');
            moviesList[movieCount].set_title();
            cout << "Enter Genre: ";
            moviesList[movieCount].set_genre();
            cout << "Enter Ticket Price: ";
            moviesList[movieCount].set_basePrice();

            movieCount++;
            saveMoviesToFile();
            cout << "\n[DONE] Movie added successfully!\n";
        }
        else
        {
            cout << "\n[!] Cinema is full! Cannot add more movies.\n";
        }
    }

    void removeMovie()
    {
        if (movieCount == 0)
        {
            cout << "No movies available to Remove.\n";
            return;
        }
        showAllMovies();
        int index;
        cout << "Enter Movie Number to remove: ";
        index = getValidNumber();
        if (index > 0 && index <= movieCount)
        {
            string filename = moviesList[index - 1].get_title() + "_seats.txt";
            filesystem::remove(filename);
            for (int i = index - 1; i < movieCount - 1; i++)
            {
                moviesList[i] = moviesList[i + 1];
            }

            movieCount--;

            saveMoviesToFile();
            cout << "[SUCCESS] Movie is removed.\n";
        }
        else
        {
            cout << "[!] Invalid Movie Number.\n";
        }
    }

    void changePrice()
    {
        if (movieCount == 0)
        {
            cout << "No movies available to update.\n";
            return;
        }
        showAllMovies();
        int index;
        cout << "Enter Movie Number to change price: ";
        index = getValidNumber();
        if (index > 0 && index <= movieCount)
        {
            cout << "Enter New Price for " << moviesList[index - 1].get_title() << ": ";
            moviesList[index - 1].set_basePrice();
            saveMoviesToFile();
            cout << "[SUCCESS] Price updated.\n";
        }
    }

    void showAllMovies()
    {
        cout << "\n--- Current Movie List ---\n";
        for (int i = 0; i < movieCount; i++)
        {
            cout << i + 1 << ". " << moviesList[i].get_title() << " (" << moviesList[i].get_genre() << ")" << " (" << moviesList[i].get_basePrice() << "$)\n";
        }
    }
};

class CinemaHall
{
private:
    Seat *seats[10][10];

public:
    CinemaHall()
    {
        for (int i = 0; i < 10; ++i)
        {
            for (int j = 0; j < 10; ++j)
            {
                if (i < 2)
                {
                    seats[i][j] = new VIP_Seat(i, j);
                }
                else
                {
                    seats[i][j] = new Regular_Seat(i, j);
                }
            }
        }
    }

    ~CinemaHall()
    {
        for (int i = 0; i < 10; ++i)
        {
            for (int j = 0; j < 10; ++j)
            {
                if (seats[i][j] != nullptr)
                {
                    delete seats[i][j];
                    seats[i][j] = nullptr;
                }
            }
        }
    }

    void resetHall()
    {
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < 10; j++)
            {
                seats[i][j]->cancelSeat(); // Wipes the seat clean
            }
        }
    }

    void saveIntoFile(string movieName)
    {
        string fileName = movieName + "_seats.txt";
        ofstream outFile(fileName);
        if (outFile.is_open())
        {
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    if (!seats[i][j]->isAvailable())
                    {
                        outFile << "1 ";
                    }
                    else
                    {
                        outFile << "0 ";
                    }
                }
                outFile << endl;
            }
            outFile.close();
        }
        else
        {
            cout << "Error: Cannot create file!" << endl;
        }
    }

    void loadFromFile(string movieName)
    {
        resetHall();

        string fileName = movieName + "_seats.txt";
        ifstream inFile(fileName);
        if (inFile.is_open())
        {
            int status;
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    if (inFile >> status)
                    {
                        if (status == 1)
                        {
                            seats[i][j]->bookSeat();
                        }
                        else
                        {
                            seats[i][j]->cancelSeat();
                        }
                    }
                }
            }
            inFile.close();
        }
        else
        {
            saveIntoFile(movieName);
        }
    }

    void displayHall(string movieTitle)
    {
        cout << "\n=========== CINEMA HALL =====================\n";

        loadFromFile(movieTitle);

        for (int i = 0; i < 10; i++)
        {
            cout << "Row " << i + 1 << " ";

            for (int j = 0; j < 10; j++)
            {
                if (seats[i][j]->isAvailable())
                {
                    cout << "[ ] ";
                }
                else
                {
                    cout << "[X] ";
                }
            }

            cout << endl;
        }

        cout << "==============================================\n";
    }

    bool bookASeat(int r, int c)
    {
        if (r < 0 || r >= 10 || c < 0 || c >= 10)
            return false;
        if (seats[r][c]->isAvailable())
        {
            seats[r][c]->bookSeat();
            return true;
        }
        return false;
    }

    bool cancelASeat(int r, int c)
    {
        if (r < 0 || r >= 10 || c < 0 || c >= 10)
            return false;
        if (!seats[r][c]->isAvailable())
        {
            seats[r][c]->cancelSeat();
            return true;
        }
        return false;
    }

    Seat *getSeatPointer(int r, int c)
    {
        if (r < 0 || r >= 10 || c < 0 || c >= 10)
            return nullptr;
        return seats[r][c];
    }
};

class Ticket
{
private:
    Movie movie;
    int row;
    int column;
    double price;

public:
    Ticket(Movie &m, int r, int c, double finalprice)
    {
        movie = m;
        row = r;
        column = c;
        price = finalprice;
    }

    void displayTicket()
    {
        cout << "\n========================================" << endl;
        cout << "           OFFICIAL RECEIPT             " << endl;
        cout << "========================================" << endl;
        cout << " Movie Title : " << movie.get_title() << endl;
        cout << " Genre       : " << movie.get_genre() << endl;
        cout << " Seat        : Row " << (row + 1) << " | Column " << (column + 1) << endl;
        cout << " Total Price : " << price << " EGP" << endl;
        cout << "========================================" << endl;
        cout << "            Enjoy your Movie             " << endl;
        cout << "========================================\n"
             << endl;
    }
};

void processBooking(AdminManager &admin, int movie_choice, CinemaHall &hall)
{
    int r, c;

    cout << "\n--- Booking Process ---" << endl;
    do
    {
        cout << "Choose your seat's row from 1-10" << endl;
        r = getValidNumber();

    } while (!(1 <= r && r <= 10));

    do
    {
        cout << "Choose your seats's coloumn from 1-10" << endl;
        c = getValidNumber();

    } while (!(1 <= c && c <= 10));

    r--;
    c--;

    if (hall.bookASeat(r, c))
    {
        Seat *seatPtr = hall.getSeatPointer(r, c);
        double finalPrice = seatPtr->calculatePrice(admin.moviesList[movie_choice - 1].get_basePrice());

        Ticket myTicket(admin.moviesList[movie_choice - 1], r, c, finalPrice);

        myTicket.displayTicket();

        hall.saveIntoFile(admin.moviesList[movie_choice - 1].get_title());
    }
    else
    {
        cout << "Error: Seat is already booked or invalid. Please try again." << endl;
    }
}

void processCancellation(AdminManager &admin, int movie_choice, CinemaHall &hall)
{
    int r, c;

    do
    {
        cout << "Enter Row (1-10): ";
        r = getValidNumber();
    } while (!(1 <= r && r <= 10));

    do
    {
        cout << "Enter Column (1-10): ";
        c = getValidNumber();
    } while (!(1 <= c && c <= 10));

    r--;
    c--;

    if (hall.cancelASeat(r, c))
    {
        cout << "Seat cancelled successfully." << endl;
        hall.saveIntoFile(admin.moviesList[movie_choice - 1].get_title());
    }
    else
    {
        cout << "Seat cancellation failed. Seat may already be free or invalid." << endl;
    }
}

int main()
{
    int choice;
    AdminManager admin;
    CinemaHall Hall1;

    cout << "\n=====================================\n";
    cout << "     CINEMA TICKET BOOKING SYSTEM    \n";
    cout << "=====================================\n";

    do
    {
        cout << "\n1. Show Movies\n";
        cout << "2. Book Ticket\n";
        cout << "3. Remove Seat\n";
        cout << "4. Admin Panel\n";
        cout << "5. Exit\n";
        cout << "Enter choice: ";

        choice = getValidNumber();

        switch (choice)
        {
        case 1:
        {
            if (admin.getMovieCount() == 0)
            {
                cout << "\nNo movies are currently playing. Please check back later.\n";
                break;
            }
            admin.showAllMovies();
            break;
        }

        case 2:
        {
            if (admin.getMovieCount() == 0)
            {
                cout << "\nNo movies available. Cannot book tickets right now.\n";
                break;
            }
            admin.showAllMovies();
            int movie_choice;

            do
            {
                cout << "\nNOTE! Rows 1 & 2 have VIP extra charge 1.4%.\n";
                cout << "\nChoose a movie from 1-" << admin.getMovieCount() << endl;
                movie_choice = getValidNumber();

            } while (!(1 <= movie_choice && movie_choice <= admin.getMovieCount()));

            Hall1.displayHall(admin.moviesList[movie_choice - 1].get_title());

            processBooking(admin, movie_choice, Hall1);

            break;
        }

        case 3:
        {
            if (admin.getMovieCount() == 0)
            {
                cout << "\nThere are no tickets to be cancelled.\n";
                break;
            }
            admin.showAllMovies();
            int movie_choice;
            do
            {
                cout << "\nChoose a movie from 1-" << admin.getMovieCount() << endl;
                movie_choice = getValidNumber();

            } while (!(1 <= movie_choice && movie_choice <= admin.getMovieCount()));

            Hall1.displayHall(admin.moviesList[movie_choice - 1].get_title());

            processCancellation(admin, movie_choice, Hall1);
            break;
        }

        case 4:
        {
            if (admin.login())
            {
                cout << "\n======= Welcome Back Admin =======" << endl;
                int back{5};
                int admin_choice;
                do
                {
                    cout << "\n1. Add Movies\n";
                    cout << "2. Remove Movies\n";
                    cout << "3. Show all movies\n";
                    cout << "4. Change price\n";
                    cout << "5. Main menu\n";
                    cout << "Enter choice: ";
                    admin_choice = getValidNumber();

                    switch (admin_choice)
                    {
                    case 1:
                        admin.addMovie();
                        break;
                    case 2:
                        admin.removeMovie();
                        break;
                    case 3:
                        admin.showAllMovies();
                        break;
                    case 4:
                        admin.changePrice();
                        break;
                    default:
                        if (admin_choice != back)
                            cout << "\nInvalid choice.\n";
                    }
                } while (admin_choice != back);
            }
            else
                cout << "\n-------Incorrect Password-------" << endl;
            break;
        }

        case 5:
        {
            cout << "\nGoodbye!\n";
            break;
        }
        default:
            cout << "\nInvalid choice.\n";
        }

    } while (choice != 5);

    return 0;
}