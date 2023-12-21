#include <stdio.h>

int min_cities_to_rebuild(int t, int n, int m) {
    // Total number of cities in the matrix
    int total_cities = n * m;

    // Cities that can be rebuilt without government aid
    int rebuilt_without_aid = 0;

    // Iterate through each test case
    for (int i = 0; i < t; i++) {
        scanf("%d %d", &n, &m);

        // Calculate rebuilt without aid in the current test case
        int internal_cities = (n - 2) * (m - 2) > 0 ? (n - 2) * (m - 2) : 0;
        int border_cities = (n - 2) * 2 + (m - 2) * 2 > 0 ? (n - 2) * 2 + (m - 2) * 2 : 0;
        rebuilt_without_aid += internal_cities + border_cities;
    }

    // Calculate the minimum number of cities the government needs to rebuild
    int min_cities = total_cities - rebuilt_without_aid;

    return min_cities;
}

int main() {
    int t, n, m;
    scanf("%d", &t);  // Number of test cases

    for (int i = 0; i < t; i++) {
        scanf("%d %d", &n, &m);  // Gridlandia size for each test case
        int result = min_cities_to_rebuild(t, n, m);
        printf("%d\n", result);
    }

    return 0;
}