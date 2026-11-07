/**
 * Google Analytics 4 Event Tracking - شركة نجوم العرب لنقل الأثاث بجدة
 * Tracks Key Events: click_call, click_whatsapp, form_submit_whatsapp
 */

(function () {
  'use strict';

  function sendGAEvent(eventName, params) {
    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, params);
    } else if (window.dataLayer && Array.isArray(window.dataLayer)) {
      window.dataLayer.push({
        event: eventName,
        ...params
      });
    }
    // Debug log in development/testing
    // console.log('[GA4 Event]', eventName, params);
  }

  // 1. Delegated Click Listener for Calls and WhatsApp
  document.addEventListener('click', function (e) {
    var target = e.target.closest('a');
    if (!target) return;

    var href = target.getAttribute('href') || '';

    // A. Phone Call Event
    if (href.startsWith('tel:')) {
      var phoneNumber = href.replace('tel:', '').trim();
      sendGAEvent('click_call', {
        event_category: 'Conversion',
        event_label: phoneNumber,
        page_location: window.location.href,
        link_text: (target.innerText || '').trim().substring(0, 50)
      });
    }

    // B. WhatsApp Click Event
    else if (href.includes('wa.me') || href.includes('whatsapp.com')) {
      sendGAEvent('click_whatsapp', {
        event_category: 'Conversion',
        event_label: 'WhatsApp Chat',
        page_location: window.location.href,
        link_text: (target.innerText || '').trim().substring(0, 50)
      });
    }
  }, true);

  // 2. Form Submission Listener (e.g. WhatsApp estimate/quote forms)
  document.addEventListener('submit', function (e) {
    var form = e.target;
    var formId = form.id || form.getAttribute('name') || 'estimate_form';
    
    sendGAEvent('form_submit_whatsapp', {
      event_category: 'Lead',
      event_label: formId,
      page_location: window.location.href
    });
  }, true);

})();
