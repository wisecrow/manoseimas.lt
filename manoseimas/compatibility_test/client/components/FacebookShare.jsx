import React from 'react'
import Button from './Button'
import styles from '../styles/components/facebook-share.css'

class FacebookShare extends React.Component {

    static propTypes = {
        responseHandler: React.PropTypes.func,
        fractions: React.PropTypes.array
    }

    constructor (props) {
        super(props)
        this.shareOnFacebook = this.shareOnFacebook.bind(this)
        this.realFractions = this.realFractions.bind(this)
    }

    // Because we have lots of TS-LDK files, it's easier just to use this function, than to convert files.
    shortTitle (fraction) {
        let short_title = fraction.short_title
        if (short_title === 'TSLKDF')
            short_title = 'TS-LKDF'
        if (short_title === 'LLRAKŠSF')
            short_title = 'LLRA-KŠSF'
        return short_title
    }

    realFractions () {
        return this.props.fractions.filter(fraction => fraction.short_title !== 'MG')
    }

    shareOnFacebook () {
        const location = window.location.href.split('/')
        const base_url = location[0] + '//' + location[2]

        // Don't include MG in facebook share results
        const fractions = this.realFractions()

        const fraction_one = fractions[0]
        const fraction_two = fractions[1]
        const fraction_three = fractions[2]

        const picture = base_url + '/static/img/fb-share/' +
                        this.shortTitle(fraction_one) + '/' +
                        this.shortTitle(fraction_two) + '-' +
                        this.shortTitle(fraction_three) + '.png'

        const caption = 'Sužinok daugiau >>>'
        const description = `${fraction_one.title} ${fraction_one.similarity}%; ` +
                            `${fraction_two.title} ${fraction_two.similarity}%; ` +
                            `${fraction_three.title} ${fraction_three.similarity}%. \n` +
                            'Su kokiomis politinėmis partijomis ir politikais sutampi tu?'

        // Track click in Google Analytics
        window.ga('send', 'event', {
            eventCategory: 'Facebook Share',
            eventAction: 'click',
            eventLabel: 'Click from Results'
        })

        FB.ui({
            method: 'feed',
            link: base_url + '/testas',
            picture: picture,
            name: 'Politinių pažiūrų testas - manoSeimas.lt',
            caption: caption,
            description: description
        }, this.props.responseHandler)
    }

    render () {
        let fractions = this.realFractions()
        return (
            <div className={styles['share-block']}>
                <header>Mano balsavimai Seime sutaptų su:</header>
                {(fractions.length > 2)
                    ? <div className={styles.fractions}>
                        <div className={styles['img-main']}>
                            <img src={fractions[0].logo} />
                        </div>
                        <div className={styles['img-second']}>
                            <img src={fractions[1].logo} />
                        </div>
                        <div className={styles['img-third']}>
                            <img src={fractions[2].logo} />
                        </div>
                    </div>
                    : ''
                }
                <Button type='facebook' action={this.shareOnFacebook}>
                    Pasidalinti
                </Button>
            </div>
        )
    }
}

export default FacebookShare
