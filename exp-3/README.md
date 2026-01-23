~ BrowserRouter
@BrowserRouter is the main wrapper for routing
@It connects your React app with the browser URL
@It uses the browser’s history back forward buttons
@without BrowserRouter routing will not work
@Usually written once in the root file 

The container that allows your app to understand URL

~ Routes
@Routes is a container for all routes
@It decides which component should be shown for a given path
@Only one route is matched at a time
@Routes replaced the old Switch in new React Router versions

A list that checks the current URL and picks the right page.

~Route
@Route defines one path and one component
If URL is this the  show this component
Written inside Routes.
Each page Home, About, Contact has its own Route.

~Link
@Link is used for navigation between pages.
@It works like tag but without page reload.
@Keeps the SPA behavior intact.
@Faster and smoother than normal anchor tags.

A smart link made for React apps.