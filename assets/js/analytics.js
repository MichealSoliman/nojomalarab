/**
 * Google Analytics 4 Event Tracking - شركة نجوم العرب لنقل الأثاث بجدة
 * Tracks Key Events: click_call, click_whatsapp, form_submit_whatsapp
 * Runs safely with or without active gtag.
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
  }

  function getSectionLocation(element) {
    var section = element.closest('header, footer, section, [id]');
    if (!section) return 'body';
    if (section.id) return section.id;
    var tagName = section.tagName.toLowerCase();
    if (tagName === 'header') return 'header';
    if (tagName === 'footer') return 'footer';
    return 'section';
  }

  // 1. Delegated Click Listener for Calls and WhatsApp
  document.addEventListener('click', function (e) {
    var target = e.target.closest('a');
    if (!target) return;

    var href = target.getAttribute('href') || '';
    var location = getSectionLocation(target);
    var linkText = (target.innerText || target.getAttribute('aria-label') || '').trim().substring(0, 50);

    // A. Phone Call Event
    if (href.startsWith('tel:')) {
      var phoneNumber = href.replace('tel:', '').trim();
      sendGAEvent('click_call', {
        event_category: 'Conversion',
        event_label: phoneNumber,
        page_location: window.location.href,
        page_path: window.location.pathname,
        link_text: linkText,
        location: location
      });
    }

    // B. WhatsApp Click Event
    else if (href.includes('wa.me') || href.includes('whatsapp.com')) {
      sendGAEvent('click_whatsapp', {
        event_category: 'Conversion',
        event_label: 'WhatsApp Chat',
        page_location: window.location.href,
        page_path: window.location.pathname,
        link_text: linkText,
        location: location
      });
    }
  }, true);

  // 2. Form Submission Listener
  document.addEventListener('submit', function (e) {
    var form = e.target;
    var formId = form.id || form.getAttribute('name') || 'contact_form';
    var location = getSectionLocation(form);

    sendGAEvent('form_submit_whatsapp', {
      event_category: 'Lead',
      event_label: formId,
      page_location: window.location.href,
      page_path: window.location.pathname,
      location: location
    });
  }, true);

})();
