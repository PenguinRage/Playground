#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "list.h"

#define BUFFERSIZE 255
#define PROMPT "> "

struct list_head * add_item( char * new_str, struct list_head * list )
{
    struct list_head * node = ( struct list_head * ) malloc( sizeof( struct list_head ) );
    char * list_str = (char *) malloc( strlen( new_str ) * sizeof( char ) );
    strcpy( list_str, new_str );
    node->item = list_str;
    list_add_tail( node, list );
    return node;
}

struct list_head * find_item( size_t it, struct list_head * list )
{
  struct list_head * node = list->next;

  if ( !list_empty( list ) )
  {
    for ( size_t el = 1; node != list; el++ )
    {
      if ( el == it )
      {
        return node;
      }
      node = node->next;
    }
  }
  return NULL;
}

void list_move( size_t src_it, size_t dest_it, struct list_head * list )
{
  if ( !list_empty( list ) )
  {
    struct list_head * src_node = find_item( src_it, list );
    struct list_head * dest_node = find_item( dest_it, list );

    if ( src_node && dest_node )
    {
      dest_node->prev->next = src_node;
      dest_node->next->prev = src_node;

      src_node->prev->next = dest_node;
      src_node->next->prev = dest_node;

      struct list_head * tmp = src_node->next;
      src_node->next = dest_node->next;
      dest_node->next = tmp;

      tmp = src_node->prev;
      src_node->prev = dest_node->prev;
      dest_node->prev = tmp;
    }
  }
}

void print_list( struct list_head * list )
{

  if ( !list_empty( list ) )
  {
    size_t el = 1;
    struct list_head * node = list->next;

    while ( node != list )
    {
      printf( "%ld. %s", el++, node->item );
      node = node->next;
    }
    printf( "\n" );
  }
}

int main( void )
{
  FILE* fp;
  if ( ( fp = fopen( "todo.txt", "r" ) ) == NULL )
  {
    perror("Could not open file.\n");
    return 1;
  }

  char str[BUFFERSIZE];
  struct list_head * list = ( struct list_head * ) malloc( sizeof( struct list_head ) );
  size_t numel = 1;

  list_init( list );
  while ( fgets( str, BUFFERSIZE, fp ) != NULL  )
  {
    add_item( str, list );
  }
  fclose( fp );

  print_list( list );

  printf( PROMPT );

  while ( fgets( str, BUFFERSIZE, stdin ) != NULL )
  {
    char command[5];
    sscanf( str, "%s", command );

    if ( !strcmp( command, "help" ) )
    {
      printf("help, new, delete, move, undo\n");
    }
    else if ( !strcmp( command, "new" ) )
    {
      char * add_str = &str[ strlen( "new" ) + 1 ];
      add_item( add_str, list );
    }
    else if ( !strcmp( command, "delete" ) )
    {
      size_t delete_it;
      sscanf( str, "%s %ld\n", command, &delete_it );

      struct list_head * node = find_item( delete_it, list );

      list_del( node );
      free( node->item );
      free( node );
    }
    else if ( !strcmp( command, "move" ) )
    {
      size_t src_it, dest_it;

      sscanf( str, "%s %ld %ld\n", command, &src_it, &dest_it );
      list_move( src_it, dest_it, list );
    }
    else if ( !strcmp( command, "undo" ) )
    {
    }

    print_list( list );
    printf( PROMPT );
  }

  fp = fopen( "todo.txt", "w" );
  while ( !list_empty( list ) )
  {
    struct list_head * next = list->next;
    list_del( next );
    fprintf( fp, "%s", next->item );
    free( next->item );
    free( next );
  }
  fclose( fp );

  return 0;
}
