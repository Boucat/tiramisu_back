# tiramisu_back
Back de tiramisu.cat

## Datalayer

### user
- id: hash of the name
- name: string
- photo: string

### restaurant
- id: hash of <name>,<lat>,<lon>
- location: geopoint
- name: string

### review

- culleretes: number
- date: timestamp
- photo: string
- review: string
- title: string
- restaurant_id: string
- user_id: string
