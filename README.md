# Shopping cart

It is a partial implementation of a shopping till system, which you might find at a supermarket.
This implementation was done by a Junior developer, you as a Senior Software Engineer have been requested to refactor this project.
You may make any technical decisions you would like, but must not change the given abstract class (abc.ShoppingCart) which is used by the shopping till hardware and cannot be easily updated.
Please treat this code as an element of a larger production system. The code is being refactored to ensure reliability and testability.

Tasks requested:
- Make the receipt print items in the order that they were added
- Add a 'Total' line to the receipt. This should be the full price we should charge the customer
- Be able to fetch product prices from an external source (json file, database ...)
- Be able to display the product prices in different currencies (not only Euro).
- Update the test suite to extend coverage and limit the number of tests which need changing when changes are introduced
- Any other changes which improve the reliability of this code in production

If you do not have enough information, make any assumptions you would like and note them down with TODO comments. Feel free to make comments that highlight completion of the tasks listed above.

Please budget 3 hours to complete, and your code should be production ready, clean and tested! Please ensure the code is version controlled also, and make sure to make several commits with sensile commit messages while working on this. When submitting please either:
- Provide a Github/GitLab/etc. link that we can view and clone your work; or
- Use git-bundle (https://git-scm.com/docs/git-bundle) to create a bundle file and send this to us.

# Changelog

## v2.0.0

### Added or Changed
- Added timestamp to product table
- Fixed typos in cart.py
- Fixed typos in test_cart.py
- Added exception handling in connection.py 
- Rename variables for better readability
- added comments wherever required 

### Removed

- Removed OrderedDict() 
- Removed import wherever not required

### Installation

1. Download Pycharm [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)
2. Clone the repo
   ```sh
   git clone https://github.com/AbdulWaheedPasha/test-shopping
   ```

3. open `test-shopping` in pycharm and Run `populate_db.py`

4. Run `tests/test_cart.py` from pycharm

