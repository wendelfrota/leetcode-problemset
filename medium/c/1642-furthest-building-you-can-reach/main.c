#include <stdio.h>
#include <stdlib.h>

void swap(int *arr, int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

typedef struct {
    int *buf;
    int cap;
    int len;
} max_heap;

void max_heap_init(max_heap *h)
{
    h->buf = malloc(32 * sizeof(int));
    h->cap = 32;
    h->len = 0;
}

void max_heapify(max_heap *h, int idx)
{
    int max_idx = idx;
    int left = 2 * idx + 1;
    int right= 2 * idx + 2;
    if (left < h->len && h->buf[left] > h->buf[max_idx]) max_idx = left;
    if (right < h->len && h->buf[right] > h->buf[max_idx]) max_idx = right;
    if (max_idx != idx)
    {
        swap(h->buf, max_idx, idx);
        max_heapify(h, max_idx);
    }
}

int max_heap_extract(max_heap *h)
{
    int res = h->buf[0];
    swap(h->buf, 0, --h->len);
    max_heapify(h, 0);
    return res;
}

void max_heap_insert(max_heap *h, int val)
{
    if (h->len == h->cap)
    {
        h->cap *= 2;
        h->buf = realloc(h->buf, h->cap * sizeof(int));
    }
    h->buf[h->len] = val;
    int idx = h->len;
    while (idx > 0 && h->buf[(idx - 1) / 2] < h->buf[idx])
    {
        swap(h->buf, idx, (idx - 1) / 2);
        idx = (idx - 1) / 2;
    }
    h->len++;
}

int max_heap_top(max_heap *h)
{
    return h->buf[0];
}


int furthestBuilding(int* heights, int heightsSize, int bricks, int ladders) {
   max_heap h;
   max_heap_init(&h);
   int i = 0;

   while (i < heightsSize - 1 && (heights[i + 1] - heights[i] <= bricks || ladders > 0))
   {
        while (i < heightsSize - 1 && heights[i + 1] - heights[i] <= bricks)
        {
            int delta;
            if ((delta = heights[i + 1] - heights[i]) > 0)
            {
                max_heap_insert(&h, delta);
                bricks -= delta;
            }
            i++;
        }

        if (i < heightsSize - 1 && ladders > 0)
        {
            if (h.len > 0 && max_heap_top(&h) > heights[i + 1] - heights[i])
                bricks += max_heap_extract(&h);
            else
                i++;

            ladders--;
        }
   }

   return i;
}

int main() {
    int heights[] = {4, 2, 7, 6, 9, 14, 12};

    printf("%d", furthestBuilding(heights, sizeof(heights)/sizeof(int), 5, 1));

    return 0;
}