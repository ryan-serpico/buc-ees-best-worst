![buc-ees-best-worst-banner.png](img/buc-ees-best-worst-banner.png)

Hey there!

This repository contains all the data and code I used to create a story for the San Antonio Express-News that searched for the best and worst Buc-ee's in Texas. It is a riff on a story concept I've done in the past with [Tim Fanning](https://www.expressnews.com/author/tim-fanning/) that looked at the best and worst [Whataburger](https://www.expressnews.com/food/article/best-worst-whataburgers-san-antonio-17415532.php) and [H-E-B](https://www.expressnews.com/business/article/best-worst-hebs-texas-mexico-17466991.php) locations in and around Texas.

**Questions answered in this analysis**:

- Where are the best and worst Buc-ee's in Texas according to ratings on Google Maps?
- What is the distribution of ratings for Buc-ee's?

## Reproducibility

If you'd like to run this notebook for yourself, you can do so by cloning this repository. 

All the required packages are listed in the `requirements.txt` file. You can install them by running the following command in your terminal:

    pip install -r requirements.txt

If you would like to run the notebooks as python files, use the `nbexec notebooks/NOTEBOOK_NAME.ipynb` command.

In order to collect your own Google map ratings, you will need to create API credentials with the [Google Cloud Platform](https://cloud.google.com/maps-platform/) and store the API key in a `.env` file.