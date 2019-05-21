#include "aoc.h"

typedef struct {
	int n;
	ListNode node;
} Marble;

int main() {
	List *l = list_new(Marble, node);

	free(l);
	printf("Hello World.\n");	
}
