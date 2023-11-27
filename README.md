# Back end for [tiramisu.cat](https://tiramisu.cat)
This is the back end for the widely popular and fully trusted [tiramisu.cat](https://tiramisu.cat) website. Where your most trusted people uploads their tiramisu reviews.

## Next steps 🧗
- Connect with Firebase
- Dockerize app
- Connect with UI
- Add tests
- Deployment management

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
